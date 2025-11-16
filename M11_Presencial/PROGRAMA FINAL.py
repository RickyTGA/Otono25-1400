"""
Réplica en Python del sistema Excel de Ricky’s (Ingredients + Master Recipe Calculator + Profit Analysis)

ACTUALIZACIÓN (fix SystemExit: 2)
- Ya no se corta con error si ejecutas el script sin argumentos. Ahora muestra la ayuda y ejemplos.
- El subcomando es opcional al inicio; si falta, se imprime la ayuda (salida 0).
- En el comando `recipe`, si omites `--recipe_csv` y no usas `--interactive`, el programa muestra un mensaje claro con ejemplos en vez de abortar.
- Se agregó `--demo` para correr una prueba rápida con los archivos de ejemplo creados en esta conversación.
- Se agregó `selftest` con tests mínimos para validar los cálculos principales.

Uso rápido:
1) Instala dependencias:  pip install pandas tabulate
2) Prepara tu Excel de ingredientes (hoja "Ingredients list") con las columnas:
   - Item Code | Product Name | Category | Stock Type | Brand | Supplier | Quantity per Package | Unit | Price in $
3) Para calcular una receta con parámetros:
   python master_calculator.py recipe --ingredients_xlsx ingredientes.xlsx \
       --recipe_csv receta.csv --servings 12 --target_food_cost_pct 30 --actual_menu_price 4.99
4) Modo interactivo de receta:
   python master_calculator.py recipe --ingredients_xlsx ingredientes.xlsx --interactive \
       --servings 12 --target_food_cost_pct 30 --actual_menu_price 4.99
5) Demo inmediata con los archivos de ejemplo (si existen en /mnt/data):
   python master_calculator.py recipe --demo
6) Análisis financiero (Profit Analysis):
   python master_calculator.py profit --sales 100000 --food_cost 36000 --labor_cost 30000 --overhead 24000 \
       --whatif_foodcost_delta_pct -5 --whatif_sales_delta_pct 3
7) Tests rápidos integrados:
   python master_calculator.py selftest

Archivos de ejemplo: ver carpeta /mnt/data creada por el asistente en esta conversación.
"""
from __future__ import annotations
import argparse
import os
import sys
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

import pandas as pd

try:
    from tabulate import tabulate
    _TAB = True
except Exception:
    _TAB = False

# ----------------------------
# A) BASE DE INGREDIENTES
# ----------------------------
@dataclass
class IngredientRow:
    item_code: Optional[str]
    product_name: str
    category: Optional[str]
    stock_type: Optional[str]
    brand: Optional[str]
    supplier: Optional[str]
    qty_per_package: float
    unit: str
    price_package: float

    @property
    def price_per_unit(self) -> float:
        return float(self.price_package) / float(self.qty_per_package) if self.qty_per_package else 0.0


class IngredientDatabase:
    REQUIRED_COLS = [
        "Item Code", "Product Name", "Category", "Stock Type", "Brand", "Supplier",
        "Quantity per Package", "Unit", "Price in $",
    ]

    def __init__(self, df: pd.DataFrame):
        missing = [c for c in self.REQUIRED_COLS if c not in df.columns]
        if missing:
            raise ValueError(f"Faltan columnas en 'Ingredients list': {missing}")
        self.df = df.copy()
        # Limpieza básica
        self.df["Product Name"] = self.df["Product Name"].astype(str).str.strip()
        self.df["Unit"] = self.df["Unit"].astype(str).str.strip().str.lower()
        for c in ["Quantity per Package", "Price in $"]:
            self.df[c] = pd.to_numeric(self.df[c], errors='coerce').fillna(0.0)
        # Índice por nombre
        self.by_name = {
            name.lower(): IngredientRow(
                item_code=(row.get("Item Code") if pd.notna(row.get("Item Code")) else None),
                product_name=name,
                category=(row.get("Category") if pd.notna(row.get("Category")) else None),
                stock_type=(row.get("Stock Type") if pd.notna(row.get("Stock Type")) else None),
                brand=(row.get("Brand") if pd.notna(row.get("Brand")) else None),
                supplier=(row.get("Supplier") if pd.notna(row.get("Supplier")) else None),
                qty_per_package=float(row["Quantity per Package"]) if pd.notna(row["Quantity per Package"]) else 0.0,
                unit=str(row["Unit"]).lower(),
                price_package=float(row["Price in $"]) if pd.notna(row["Price in $"]) else 0.0,
            )
            for _, row in self.df.iterrows()
            for name in [str(row["Product Name"]).strip()]
            if name
        }

    def unit_price(self, product_name: str) -> Tuple[float, str]:
        key = product_name.strip().lower()
        if key not in self.by_name:
            raise KeyError(f"Ingrediente no encontrado en base: {product_name}")
        ing = self.by_name[key]
        return ing.price_per_unit, ing.unit

    def suggest(self, prefix: str, k: int = 10) -> List[str]:
        p = prefix.lower()
        return [name for name in self.by_name.keys() if name.startswith(p)][:k]


# ----------------------------
# B) MASTER RECIPE CALCULATOR
# ----------------------------
@dataclass
class RecipeLine:
    ingredient: str
    quantity: float
    unit: Optional[str] = None


def normalize_unit(u: Optional[str]) -> Optional[str]:
    if u is None or (isinstance(u, float) and pd.isna(u)):
        return None
    return str(u).strip().lower()


class MasterCalculator:
    def __init__(self, db: IngredientDatabase):
        self.db = db

    def compute(self,
                lines: List[RecipeLine],
                servings: float,
                target_food_cost_pct: float,
                actual_menu_price: Optional[float] = None) -> Dict:
        rows = []
        total_cost = 0.0
        for line in lines:
            unit_price, base_unit = self.db.unit_price(line.ingredient)
            unit_in = normalize_unit(line.unit) or base_unit
            # Réplica exacta: la unidad debe coincidir con la base
            if unit_in != base_unit:
                raise ValueError(
                    f"Unidad distinta a la base para '{line.ingredient}'. Base: {base_unit} / Ingresada: {unit_in}. "
                    "Para la réplica A exigimos coincidencia exacta."
                )
            cost = unit_price * float(line.quantity)
            total_cost += cost
            rows.append({
                "ingredient": line.ingredient,
                "quantity": line.quantity,
                "unit": unit_in,
                "ingredient_cost": round(cost, 2),
            })
        # Análisis por ingrediente
        for r in rows:
            r["ingredient_cost_pct"] = round((r["ingredient_cost"] / total_cost * 100.0), 2) if total_cost else 0.0
        cost_per_serving = total_cost / float(servings) if servings else 0.0
        target_menu_price = cost_per_serving / (target_food_cost_pct / 100.0) if target_food_cost_pct > 0 else 0.0
        result = {
            "lines": rows,
            "recipe_order_cost": round(total_cost, 2),
            "cost_per_serving": round(cost_per_serving, 2),
            "target_food_cost_pct": round(target_food_cost_pct, 2),
            "target_menu_price": round(target_menu_price, 2),
        }
        if actual_menu_price is not None:
            actual_fc_pct = (cost_per_serving / actual_menu_price * 100.0) if actual_menu_price else 0.0
            result.update({
                "actual_menu_price": round(actual_menu_price, 2),
                "actual_food_cost_pct": round(actual_fc_pct, 1),
                "target_gross_profit": round(target_menu_price - cost_per_serving, 2),
                "target_gross_profit_pct": round(((target_menu_price - cost_per_serving) / target_menu_price * 100.0) if target_menu_price else 0.0, 1),
                "actual_gross_profit": round(actual_menu_price - cost_per_serving, 2),
                "actual_gross_profit_pct": round(((actual_menu_price - cost_per_serving) / actual_menu_price * 100.0) if actual_menu_price else 0.0, 1),
            })
        return result

    @staticmethod
    def print_result(res: Dict):
        df = pd.DataFrame(res.get("lines", []))
        if _TAB and not df.empty:
            print("\nIngredientes:")
            print(tabulate(df, headers="keys", tablefmt="github", showindex=False))
        elif not df.empty:
            print(df.to_string(index=False))
        print("\nTOTALES:")
        for k in ["recipe_order_cost", "cost_per_serving", "target_menu_price"]:
            if k in res:
                print(f"{k.replace('_',' ').title()}: ${res[k]}")
        extra = [
            "actual_food_cost_pct", "actual_menu_price", "target_gross_profit", "target_gross_profit_pct",
            "actual_gross_profit", "actual_gross_profit_pct"
        ]
        for k in extra:
            if k in res:
                lbl = k.replace('_',' ').title()
                if k.endswith('_pct'):
                    print(f"{lbl}: {res[k]}%")
                else:
                    print(f"{lbl}: ${res[k]}")


# ----------------------------
# C) PROFIT ANALYSIS
# ----------------------------
@dataclass
class ProfitInput:
    sales: float
    food_cost: float
    labor_cost: float
    overhead: float
    whatif_foodcost_delta_pct: Optional[float] = None  # p.ej. -5 para bajar 5%
    whatif_sales_delta_pct: Optional[float] = None     # p.ej. +3 para subir 3%


def profit_analysis(inp: ProfitInput) -> Dict:
    prime_costs = inp.food_cost + inp.labor_cost
    total_costs = prime_costs + inp.overhead
    profit = inp.sales - total_costs

    pct = lambda x: (x / inp.sales * 100.0) if inp.sales else 0.0

    res = {
        "sales": round(inp.sales, 2),
        "food_cost": round(inp.food_cost, 2),
        "food_cost_pct": round(pct(inp.food_cost), 1),
        "labor_cost": round(inp.labor_cost, 2),
        "labor_cost_pct": round(pct(inp.labor_cost), 1),
        "prime_costs": round(prime_costs, 2),
        "prime_costs_pct": round(pct(prime_costs), 1),
        "overhead": round(inp.overhead, 2),
        "overhead_pct": round(pct(inp.overhead), 1),
        "total_costs": round(total_costs, 2),
        "total_costs_pct": round(pct(total_costs), 1),
        "profit": round(profit, 2),
        "profit_pct": round(pct(profit), 1),
    }

    # Escenarios What-if
    if inp.whatif_foodcost_delta_pct is not None:
        delta = inp.food_cost * (inp.whatif_foodcost_delta_pct / 100.0)
        res["whatif_foodcost_profit_delta"] = round(-delta, 2)  # reducir costo aumenta utilidad
    if inp.whatif_sales_delta_pct is not None:
        delta = inp.sales * (inp.whatif_sales_delta_pct / 100.0)
        res["whatif_sales_profit_delta"] = round(delta, 2)

    return res


def print_profit(res: Dict):
    if _TAB:
        tbl = [
            ["Sales", res['sales'], f"{100.0}%"],
            ["Food Costs", res['food_cost'], f"{res['food_cost_pct']}%"],
            ["Labor Costs", res['labor_cost'], f"{res['labor_cost_pct']}%"],
            ["Prime Costs", res['prime_costs'], f"{res['prime_costs_pct']}%"],
            ["Overhead", res['overhead'], f"{res['overhead_pct']}%"],
            ["Total Costs", res['total_costs'], f"{res['total_costs_pct']}%"],
            ["Profit", res['profit'], f"{res['profit_pct']}%"],
        ]
        print(tabulate(tbl, headers=["Item","Amount","% of Sales"], tablefmt="github"))
    else:
        print(res)
    if "whatif_foodcost_profit_delta" in res:
        print(f"\nReducir food cost segun escenario => +${res['whatif_foodcost_profit_delta']} de utilidad")
    if "whatif_sales_profit_delta" in res:
        print(f"Aumentar ventas segun escenario => +${res['whatif_sales_profit_delta']} de utilidad")


# ----------------------------
# IO helpers
# ----------------------------

def read_ingredients_xlsx(path: str, sheet_name: str = "Ingredients list") -> IngredientDatabase:
    df = pd.read_excel(path, sheet_name=sheet_name)
    return IngredientDatabase(df)


def read_recipe_csv(path: str) -> List[RecipeLine]:
    df = pd.read_csv(path)
    need = {"ingredient","quantity","unit"}
    miss = need - set(df.columns)
    if miss:
        raise ValueError(f"El CSV de receta debe tener columnas {need}. Faltan: {miss}")
    lines: List[RecipeLine] = []
    for _, r in df.iterrows():
        if pd.isna(r["ingredient"]) or pd.isna(r["quantity"]):
            continue
        lines.append(RecipeLine(
            ingredient=str(r["ingredient"]).strip(),
            quantity=float(r["quantity"]),
            unit=str(r["unit"]).strip() if pd.notna(r["unit"]) else None,
        ))
    return lines


# ----------------------------
# CLI y tests
# ----------------------------

def _build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Réplica Python del Excel de recetas y análisis de Ricky’s", add_help=True)
    sub = p.add_subparsers(dest="cmd")  # no 'required': manejamos la ayuda manualmente

    # recipe
    pr = sub.add_parser("recipe", help="Calcular receta (Master Calculator)")
    pr.add_argument("--ingredients_xlsx")
    pr.add_argument("--ingredients_sheet", default="Ingredients list")
    pr.add_argument("--recipe_csv")
    pr.add_argument("--interactive", action="store_true")
    pr.add_argument("--servings", type=float, default=1.0)
    pr.add_argument("--target_food_cost_pct", type=float, default=30.0)
    pr.add_argument("--actual_menu_price", type=float)
    pr.add_argument("--demo", action="store_true", help="Usar archivos de ejemplo si están disponibles")

    # profit
    pp = sub.add_parser("profit", help="Análisis financiero tipo Profit Analysis")
    pp.add_argument("--sales", type=float)
    pp.add_argument("--food_cost", type=float)
    pp.add_argument("--labor_cost", type=float)
    pp.add_argument("--overhead", type=float)
    pp.add_argument("--whatif_foodcost_delta_pct", type=float)
    pp.add_argument("--whatif_sales_delta_pct", type=float)

    # selftest
    sub.add_parser("selftest", help="Ejecuta tests mínimos integrados")
    return p


def _print_examples():
    examples = """
Ejemplos:
  python master_calculator.py recipe --ingredients_xlsx ingredients.xlsx \
      --recipe_csv receta.csv --servings 12 --target_food_cost_pct 30 --actual_menu_price 4.99
  python master_calculator.py recipe --ingredients_xlsx ingredients.xlsx --interactive \
      --servings 12 --target_food_cost_pct 30 --actual_menu_price 4.99
  python master_calculator.py recipe --demo
  python master_calculator.py profit --sales 100000 --food_cost 36000 --labor_cost 30000 --overhead 24000 \
      --whatif_foodcost_delta_pct -5 --whatif_sales_delta_pct 3
  python master_calculator.py selftest
"""
    print(examples)


def main(argv: Optional[List[str]] = None) -> int:
    parser = _build_arg_parser()
    argv = sys.argv[1:] if argv is None else argv
    if not argv:
        parser.print_help()
        _print_examples()
        return 0

    args = parser.parse_args(argv)

    if args.cmd is None:
        parser.print_help()
        _print_examples()
        return 0

    if args.cmd == "recipe":
        # DEMO rápida si se solicita
        if getattr(args, "demo", False):
            demo_ing = "/mnt/data/ingredients_list_example.xlsx"
            demo_rec = "/mnt/data/receta_example.csv"
            if not (os.path.exists(demo_ing) and os.path.exists(demo_rec)):
                print("No se encontraron archivos de demo en /mnt/data. Usa --ingredients_xlsx y --recipe_csv.")
                return 2
            args.ingredients_xlsx = demo_ing
            args.recipe_csv = demo_rec
            args.servings = 12
            args.target_food_cost_pct = 30
            args.actual_menu_price = 4.99

        if not args.ingredients_xlsx:
            print("Falta --ingredients_xlsx. Consulta los ejemplos de uso.")
            _print_examples()
            return 2

        db = read_ingredients_xlsx(args.ingredients_xlsx, args.ingredients_sheet)
        calc = MasterCalculator(db)

        if args.interactive:
            print("\nEscribe lineas como 'ingrediente,cantidad,unidad' y 'fin' para terminar.")
            lines: List[RecipeLine] = []
            while True:
                s = input("> ").strip()
                if s.lower() in {"fin","salir","exit"}:
                    break
                try:
                    ing, qty, unit = [x.strip() for x in s.split(",")]
                    lines.append(RecipeLine(ing, float(qty), unit))
                except Exception:
                    print("Formato: ingrediente,cantidad,unidad")
            res = calc.compute(lines, args.servings, args.target_food_cost_pct, args.actual_menu_price)
            MasterCalculator.print_result(res)
            return 0
        else:
            if not args.recipe_csv:
                print("Falta --recipe_csv o usa --interactive. Mira estos ejemplos:")
                _print_examples()
                return 2
            lines = read_recipe_csv(args.recipe_csv)
            res = calc.compute(lines, args.servings, args.target_food_cost_pct, args.actual_menu_price)
            MasterCalculator.print_result(res)
            return 0

    if args.cmd == "profit":
        need = ["sales","food_cost","labor_cost","overhead"]
        missing = [n for n in need if getattr(args, n) is None]
        if missing:
            print(f"Faltan argumentos: {missing}. Ejemplo:")
            _print_examples()
            return 2
        res = profit_analysis(ProfitInput(
            sales=args.sales,
            food_cost=args.food_cost,
            labor_cost=args.labor_cost,
            overhead=args.overhead,
            whatif_foodcost_delta_pct=args.whatif_foodcost_delta_pct,
            whatif_sales_delta_pct=args.whatif_sales_delta_pct,
        ))
        print_profit(res)
        return 0

    if args.cmd == "selftest":
        # Tests mínimos (añadidos porque no existían)
        # 1) Base de ingredientes simple
        df = pd.DataFrame({
            "Item Code": ["B01","E01"],
            "Product Name": ["Bacon","Eggs"],
            "Category": ["Meat","Dairy"],
            "Stock Type": ["Dry","Dry"],
            "Brand": ["-","-"],
            "Supplier": ["Main","Main"],
            "Quantity per Package": [10,12],
            "Unit": ["pcs","pcs"],
            "Price in $": [10.0,6.0],
        })
        db = IngredientDatabase(df)
        # 2) Receta típica (igual a tu ejemplo: 3 bacon + 2 eggs, 12 porciones)
        calc = MasterCalculator(db)
        res = calc.compute([
            RecipeLine("Bacon", 3, "pcs"),
            RecipeLine("Eggs", 2, "pcs"),
        ], servings=12, target_food_cost_pct=30, actual_menu_price=4.99)
        # Asserts
        assert res["recipe_order_cost"] == 4.0, res
        assert res["cost_per_serving"] == 0.33, res
        assert res["target_menu_price"] == 1.11, res
        assert res["actual_food_cost_pct"] == 6.7, res
        print("SELFTEST OK: cálculos principales coinciden con el Excel.")
        return 0

    # Si llegamos aquí, mostramos ayuda por seguridad
    parser.print_help()
    _print_examples()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
