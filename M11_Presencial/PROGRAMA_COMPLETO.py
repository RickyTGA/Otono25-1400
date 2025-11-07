"""
PROGRAMA COMPLETO - Sistema de Gestión de Recetas para Negocios
Versión mejorada que guía al usuario paso a paso desde el registro de productos

Autor: Ricky's Recipe System
Fecha: Noviembre 2025
"""

import os
import sys
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

try:
    import pandas as pd
    _PANDAS = True
except ImportError:
    _PANDAS = False
    print("⚠️  Instalando pandas...")
    os.system("pip install pandas")

try:
    from tabulate import tabulate
    _TABULATE = True
except ImportError:
    _TABULATE = False
    print("⚠️  Instalando tabulate...")
    os.system("pip install tabulate")

@dataclass
class Ingrediente:
    """Clase para representar un ingrediente del negocio"""
    codigo: str
    nombre: str
    categoria: str
    marca: str
    proveedor: str
    cantidad_paquete: float
    unidad: str
    precio_paquete: float
    calorias_por_unidad: float = 0.0  # Calorías por unidad (ej: por 100g, por pieza)
    proteinas_por_unidad: float = 0.0  # Gramos de proteína por unidad
    carbohidratos_por_unidad: float = 0.0  # Gramos de carbohidratos por unidad
    grasas_por_unidad: float = 0.0  # Gramos de grasas por unidad
    
    @property
    def precio_por_unidad(self) -> float:
        """Calcula el precio por unidad"""
        return self.precio_paquete / self.cantidad_paquete if self.cantidad_paquete > 0 else 0.0

class BaseDatosIngredientes:
    """Base de datos de ingredientes del negocio"""
    
    def __init__(self):
        self.ingredientes: Dict[str, Ingrediente] = {}
    
    def agregar_ingrediente(self, ingrediente: Ingrediente):
        """Agrega un ingrediente a la base de datos"""
        self.ingredientes[ingrediente.nombre.lower()] = ingrediente
    
    def buscar_ingrediente(self, nombre: str) -> Optional[Ingrediente]:
        """Busca un ingrediente por nombre"""
        return self.ingredientes.get(nombre.lower())
    
    def listar_ingredientes(self):
        """Lista todos los ingredientes registrados"""
        if not self.ingredientes:
            print("❌ No hay ingredientes registrados aún.")
            return
        
        print("\n📋 INGREDIENTES REGISTRADOS:")
        print("-" * 80)
        for ingrediente in self.ingredientes.values():
            print(f"• {ingrediente.nombre} ({ingrediente.categoria})")
            print(f"  Precio: ${ingrediente.precio_paquete:.2f} por {ingrediente.cantidad_paquete} {ingrediente.unidad}")
            print(f"  Precio unitario: ${ingrediente.precio_por_unidad:.2f} por {ingrediente.unidad}")
            if ingrediente.calorias_por_unidad > 0:
                print(f"  Información nutricional por {ingrediente.unidad}:")
                print(f"    • Calorías: {ingrediente.calorias_por_unidad:.1f} kcal")
                if ingrediente.proteinas_por_unidad > 0:
                    print(f"    • Proteínas: {ingrediente.proteinas_por_unidad:.1f}g")
                if ingrediente.carbohidratos_por_unidad > 0:
                    print(f"    • Carbohidratos: {ingrediente.carbohidratos_por_unidad:.1f}g")
                if ingrediente.grasas_por_unidad > 0:
                    print(f"    • Grasas: {ingrediente.grasas_por_unidad:.1f}g")
            print()

@dataclass
class LineaReceta:
    """Línea de una receta"""
    ingrediente: str
    cantidad: float
    unidad: str

class CalculadoraRecetas:
    """Calculadora principal de recetas y costos"""
    
    def __init__(self, base_datos: BaseDatosIngredientes):
        self.base_datos = base_datos
    
    def calcular_receta(self, 
                       lineas: List[LineaReceta], 
                       porciones: int,
                       objetivo_costo_comida_pct: float,
                       precio_menu_actual: Optional[float] = None) -> Dict:
        """Calcula los costos de una receta"""
        
        if not lineas:
            raise ValueError("La receta no puede estar vacía")
        
        detalles_ingredientes = []
        costo_total = 0.0
        calorias_totales = 0.0
        proteinas_totales = 0.0
        carbohidratos_totales = 0.0
        grasas_totales = 0.0
        
        for linea in lineas:
            ingrediente = self.base_datos.buscar_ingrediente(linea.ingrediente)
            if not ingrediente:
                raise ValueError(f"Ingrediente '{linea.ingrediente}' no encontrado en la base de datos")
            
            # Verificar que las unidades coincidan
            if linea.unidad.lower() != ingrediente.unidad.lower():
                raise ValueError(f"Unidad incorrecta para '{linea.ingrediente}'. Use: {ingrediente.unidad}")
            
            costo_ingrediente = ingrediente.precio_por_unidad * linea.cantidad
            costo_total += costo_ingrediente
            
            # Cálculos nutricionales
            calorias_ingrediente = ingrediente.calorias_por_unidad * linea.cantidad
            proteinas_ingrediente = ingrediente.proteinas_por_unidad * linea.cantidad
            carbohidratos_ingrediente = ingrediente.carbohidratos_por_unidad * linea.cantidad
            grasas_ingrediente = ingrediente.grasas_por_unidad * linea.cantidad
            
            calorias_totales += calorias_ingrediente
            proteinas_totales += proteinas_ingrediente
            carbohidratos_totales += carbohidratos_ingrediente
            grasas_totales += grasas_ingrediente
            
            detalles_ingredientes.append({
                "ingrediente": linea.ingrediente,
                "cantidad": linea.cantidad,
                "unidad": linea.unidad,
                "precio_unitario": round(ingrediente.precio_por_unidad, 2),
                "costo_ingrediente": round(costo_ingrediente, 2),
                "calorias": round(calorias_ingrediente, 1),
                "proteinas": round(proteinas_ingrediente, 1),
                "carbohidratos": round(carbohidratos_ingrediente, 1),
                "grasas": round(grasas_ingrediente, 1)
            })
        
        # Calcular porcentajes por ingrediente
        for detalle in detalles_ingredientes:
            detalle["porcentaje_costo"] = round((detalle["costo_ingrediente"] / costo_total * 100), 2) if costo_total > 0 else 0
        
        # Cálculos principales
        costo_por_porcion = costo_total / porciones if porciones > 0 else 0
        precio_objetivo = costo_por_porcion / (objetivo_costo_comida_pct / 100) if objetivo_costo_comida_pct > 0 else 0
        
        # Cálculos nutricionales por porción
        calorias_por_porcion = calorias_totales / porciones if porciones > 0 else 0
        proteinas_por_porcion = proteinas_totales / porciones if porciones > 0 else 0
        carbohidratos_por_porcion = carbohidratos_totales / porciones if porciones > 0 else 0
        grasas_por_porcion = grasas_totales / porciones if porciones > 0 else 0
        
        resultado = {
            "detalles_ingredientes": detalles_ingredientes,
            "costo_total_receta": round(costo_total, 2),
            "costo_por_porcion": round(costo_por_porcion, 2),
            "porciones": porciones,
            "objetivo_costo_comida_pct": objetivo_costo_comida_pct,
            "precio_objetivo": round(precio_objetivo, 2),
            # Información nutricional
            "calorias_totales": round(calorias_totales, 1),
            "proteinas_totales": round(proteinas_totales, 1),
            "carbohidratos_totales": round(carbohidratos_totales, 1),
            "grasas_totales": round(grasas_totales, 1),
            "calorias_por_porcion": round(calorias_por_porcion, 1),
            "proteinas_por_porcion": round(proteinas_por_porcion, 1),
            "carbohidratos_por_porcion": round(carbohidratos_por_porcion, 1),
            "grasas_por_porcion": round(grasas_por_porcion, 1),
        }
        
        # Si se proporciona precio actual del menú
        if precio_menu_actual is not None:
            costo_comida_actual_pct = (costo_por_porcion / precio_menu_actual * 100) if precio_menu_actual > 0 else 0
            ganancia_bruta = precio_menu_actual - costo_por_porcion
            ganancia_bruta_pct = (ganancia_bruta / precio_menu_actual * 100) if precio_menu_actual > 0 else 0
            
            resultado.update({
                "precio_menu_actual": precio_menu_actual,
                "costo_comida_actual_pct": round(costo_comida_actual_pct, 2),
                "ganancia_bruta": round(ganancia_bruta, 2),
                "ganancia_bruta_pct": round(ganancia_bruta_pct, 2)
            })
        
        return resultado

def mostrar_titulo():
    """Muestra el título del programa"""
    print("=" * 80)
    print("🍽️  SISTEMA DE GESTIÓN DE RECETAS PARA NEGOCIOS")
    print("    Calcula costos, precios y rentabilidad de tus recetas")
    print("=" * 80)
    print()

def registrar_ingredientes(base_datos: BaseDatosIngredientes):
    """Función para registrar ingredientes del negocio"""
    print("📦 REGISTRO DE INGREDIENTES/PRODUCTOS")
    print("Vamos a registrar los ingredientes que utilizas en tu negocio.")
    print("Presiona Enter sin escribir nada en 'nombre' para terminar.\n")
    
    while True:
        print("-" * 50)
        nombre = input("Nombre del ingrediente: ").strip()
        if not nombre:
            break
        
        # Verificar si ya existe
        if base_datos.buscar_ingrediente(nombre):
            print(f"⚠️  El ingrediente '{nombre}' ya está registrado.")
            continue
        
        try:
            codigo = input("Código del producto (opcional): ").strip() or f"AUTO-{len(base_datos.ingredientes)+1:03d}"
            categoria = input("Categoría (ej: Carnes, Verduras, Lácteos): ").strip() or "General"
            marca = input("Marca (opcional): ").strip() or "Sin marca"
            proveedor = input("Proveedor (opcional): ").strip() or "Sin proveedor"
            
            cantidad_paquete = float(input("Cantidad por paquete/bolsa: "))
            unidad = input("Unidad (ej: kg, litros, pcs, gramos): ").strip().lower()
            precio_paquete = float(input("Precio del paquete completo ($): "))
            
            # Información nutricional (opcional)
            print("\n🥗 INFORMACIÓN NUTRICIONAL (Opcional - por unidad)")
            print("Presiona Enter para omitir cualquier valor nutricional")
            
            calorias_str = input(f"Calorías por {unidad} (ej: 250): ").strip()
            calorias = float(calorias_str) if calorias_str else 0.0
            
            proteinas_str = input(f"Proteínas en gramos por {unidad} (ej: 15.5): ").strip()
            proteinas = float(proteinas_str) if proteinas_str else 0.0
            
            carbohidratos_str = input(f"Carbohidratos en gramos por {unidad} (ej: 30.2): ").strip()
            carbohidratos = float(carbohidratos_str) if carbohidratos_str else 0.0
            
            grasas_str = input(f"Grasas en gramos por {unidad} (ej: 8.1): ").strip()
            grasas = float(grasas_str) if grasas_str else 0.0
            
            ingrediente = Ingrediente(
                codigo=codigo,
                nombre=nombre,
                categoria=categoria,
                marca=marca,
                proveedor=proveedor,
                cantidad_paquete=cantidad_paquete,
                unidad=unidad,
                precio_paquete=precio_paquete,
                calorias_por_unidad=calorias,
                proteinas_por_unidad=proteinas,
                carbohidratos_por_unidad=carbohidratos,
                grasas_por_unidad=grasas
            )
            
            base_datos.agregar_ingrediente(ingrediente)
            print(f"✅ Ingrediente '{nombre}' registrado exitosamente!")
            print(f"   Precio por {unidad}: ${ingrediente.precio_por_unidad:.2f}")
            if calorias > 0:
                print(f"   Calorías por {unidad}: {calorias:.1f} kcal")
            print()
        except ValueError:
            print("❌ Error: Ingresa números válidos para cantidad y precio.")
        except Exception as e:
            print(f"❌ Error: {e}")

def crear_receta(base_datos: BaseDatosIngredientes, calculadora: CalculadoraRecetas):
    """Función para crear y calcular una receta"""
    print("\n🍳 CREADOR DE RECETAS")
    print("Vamos a crear una receta con tus ingredientes registrados.")
    
    # Mostrar ingredientes disponibles
    base_datos.listar_ingredientes()
    
    if not base_datos.ingredientes:
        print("❌ Necesitas registrar ingredientes primero.")
        return
    
    print("\nIngresa los ingredientes de tu receta.")
    print("Presiona Enter sin escribir nada en 'ingrediente' para terminar.\n")
    
    lineas_receta = []
    
    while True:
        print("-" * 40)
        nombre_ingrediente = input("Nombre del ingrediente: ").strip()
        if not nombre_ingrediente:
            break
        
        ingrediente = base_datos.buscar_ingrediente(nombre_ingrediente)
        if not ingrediente:
            print(f"❌ Ingrediente '{nombre_ingrediente}' no encontrado.")
            print("Ingredientes disponibles:")
            for nombre in base_datos.ingredientes.keys():
                print(f"  • {nombre}")
            continue
        
        try:
            cantidad = float(input(f"Cantidad ({ingrediente.unidad}): "))
            unidad = ingrediente.unidad  # Usar la unidad del ingrediente registrado
            
            linea = LineaReceta(nombre_ingrediente, cantidad, unidad)
            lineas_receta.append(linea)
            print(f"✅ Agregado: {cantidad} {unidad} de {nombre_ingrediente}")
            
        except ValueError:
            print("❌ Error: Ingresa un número válido para la cantidad.")
    
    if not lineas_receta:
        print("❌ No se agregaron ingredientes a la receta.")
        return
    
    # Parámetros de la receta
    print("\n📊 PARÁMETROS DE CÁLCULO")
    try:
        porciones = int(input("¿Cuántas porciones produce esta receta?: "))
        objetivo_costo_pct = float(input("¿Qué porcentaje de costo de comida deseas? (ej: 30): "))
        
        precio_actual_input = input("¿Cuál es el precio actual del menú? (opcional, presiona Enter para omitir): $").strip()
        precio_actual = float(precio_actual_input) if precio_actual_input else None
        
        # Calcular la receta
        resultado = calculadora.calcular_receta(lineas_receta, porciones, objetivo_costo_pct, precio_actual)
        mostrar_resultado_receta(resultado)
        
    except ValueError:
        print("❌ Error: Ingresa números válidos.")
    except Exception as e:
        print(f"❌ Error al calcular la receta: {e}")

def mostrar_resultado_receta(resultado: Dict):
    """Muestra los resultados del cálculo de la receta"""
    print("\n" + "="*60)
    print("📋 RESULTADOS DE LA RECETA")
    print("="*60)
    
    # Tabla de ingredientes
    if _TABULATE:
        headers = ["Ingrediente", "Cantidad", "Unidad", "$/Unidad", "Costo", "%", "Calorías"]
        tabla = []
        for detalle in resultado["detalles_ingredientes"]:
            tabla.append([
                detalle["ingrediente"],
                detalle["cantidad"],
                detalle["unidad"],
                f"${detalle['precio_unitario']:.2f}",
                f"${detalle['costo_ingrediente']:.2f}",
                f"{detalle['porcentaje_costo']:.1f}%",
                f"{detalle['calorias']:.1f} kcal" if detalle['calorias'] > 0 else "N/A"
            ])
        print("\n📦 INGREDIENTES:")
        print(tabulate(tabla, headers=headers, tablefmt="grid"))
    else:
        print("\n📦 INGREDIENTES:")
        for detalle in resultado["detalles_ingredientes"]:
            calorias_text = f" ({detalle['calorias']:.1f} kcal)" if detalle['calorias'] > 0 else ""
            print(f"• {detalle['ingrediente']}: {detalle['cantidad']} {detalle['unidad']} "
                  f"= ${detalle['costo_ingrediente']:.2f} ({detalle['porcentaje_costo']:.1f}%){calorias_text}")
    
    # Resumen financiero
    print(f"\n💰 RESUMEN FINANCIERO:")
    print(f"   Costo total de la receta: ${resultado['costo_total_receta']:.2f}")
    print(f"   Porciones: {resultado['porciones']}")
    print(f"   Costo por porción: ${resultado['costo_por_porcion']:.2f}")
    print(f"   Objetivo % costo comida: {resultado['objetivo_costo_comida_pct']:.1f}%")
    print(f"   Precio objetivo recomendado: ${resultado['precio_objetivo']:.2f}")
    
    # Información nutricional
    if resultado['calorias_totales'] > 0:
        print(f"\n🥗 INFORMACIÓN NUTRICIONAL:")
        print(f"   Total de la receta completa:")
        print(f"     • Calorías: {resultado['calorias_totales']:.1f} kcal")
        if resultado['proteinas_totales'] > 0:
            print(f"     • Proteínas: {resultado['proteinas_totales']:.1f}g")
        if resultado['carbohidratos_totales'] > 0:
            print(f"     • Carbohidratos: {resultado['carbohidratos_totales']:.1f}g")
        if resultado['grasas_totales'] > 0:
            print(f"     • Grasas: {resultado['grasas_totales']:.1f}g")
        
        print(f"\n   Por porción ({resultado['porciones']} porciones):")
        print(f"     • Calorías: {resultado['calorias_por_porcion']:.1f} kcal")
        if resultado['proteinas_por_porcion'] > 0:
            print(f"     • Proteínas: {resultado['proteinas_por_porcion']:.1f}g")
        if resultado['carbohidratos_por_porcion'] > 0:
            print(f"     • Carbohidratos: {resultado['carbohidratos_por_porcion']:.1f}g")
        if resultado['grasas_por_porcion'] > 0:
            print(f"     • Grasas: {resultado['grasas_por_porcion']:.1f}g")
        
        # Clasificación calórica
        calorias_porcion = resultado['calorias_por_porcion']
        if calorias_porcion > 0:
            if calorias_porcion < 200:
                categoria_calorica = "🟢 Bajo en calorías"
            elif calorias_porcion < 400:
                categoria_calorica = "🟡 Moderado en calorías"
            elif calorias_porcion < 600:
                categoria_calorica = "🟠 Alto en calorías"
            else:
                categoria_calorica = "🔴 Muy alto en calorías"
            print(f"\n   📊 Clasificación: {categoria_calorica}")
    
    if "precio_menu_actual" in resultado:
        print(f"\n📊 ANÁLISIS ACTUAL:")
        print(f"   Precio actual del menú: ${resultado['precio_menu_actual']:.2f}")
        print(f"   % real de costo comida: {resultado['costo_comida_actual_pct']:.1f}%")
        print(f"   Ganancia bruta por porción: ${resultado['ganancia_bruta']:.2f}")
        print(f"   % ganancia bruta: {resultado['ganancia_bruta_pct']:.1f}%")
        
        # Recomendaciones
        if resultado['costo_comida_actual_pct'] > resultado['objetivo_costo_comida_pct']:
            print(f"\n⚠️  RECOMENDACIÓN: Tu costo de comida ({resultado['costo_comida_actual_pct']:.1f}%) "
                  f"está por encima del objetivo ({resultado['objetivo_costo_comida_pct']:.1f}%). "
                  f"Considera subir el precio a ${resultado['precio_objetivo']:.2f}")
        else:
            print(f"\n✅ EXCELENTE: Tu costo de comida está bajo control.")

def mostrar_tabla_calorias():
    """Muestra una tabla de referencia de calorías por alimentos comunes"""
    print("\n" + "="*70)
    print("🥗 TABLA DE REFERENCIA DE CALORÍAS")
    print("   (Valores aproximados por cada 100g o unidad)")
    print("="*70)
    
    alimentos_referencia = [
        # Carnes y proteínas
        ("🥩 CARNES Y PROTEÍNAS", ""),
        ("Pollo (pechuga sin piel)", "165 kcal, 31g proteína, 0g carb, 3.6g grasa"),
        ("Carne de res (magra)", "250 kcal, 26g proteína, 0g carb, 15g grasa"),
        ("Cerdo (lomo)", "242 kcal, 27g proteína, 0g carb, 14g grasa"),
        ("Pescado (salmón)", "208 kcal, 25g proteína, 0g carb, 12g grasa"),
        ("Huevos (por unidad)", "70 kcal, 6g proteína, 1g carb, 5g grasa"),
        
        ("", ""),
        ("🥛 LÁCTEOS", ""),
        ("Leche entera (100ml)", "61 kcal, 3.2g proteína, 4.5g carb, 3.25g grasa"),
        ("Queso cheddar", "402 kcal, 25g proteína, 1.3g carb, 33g grasa"),
        ("Yogurt natural", "59 kcal, 10g proteína, 3.6g carb, 0.4g grasa"),
        
        ("", ""),
        ("🥖 CEREALES Y GRANOS", ""),
        ("Arroz blanco (cocido)", "130 kcal, 2.7g proteína, 28g carb, 0.3g grasa"),
        ("Pan integral (por rebanada)", "69 kcal, 3.6g proteína, 12g carb, 1.2g grasa"),
        ("Pasta (cocida)", "131 kcal, 5g proteína, 25g carb, 1.1g grasa"),
        ("Harina de trigo", "364 kcal, 10g proteína, 76g carb, 1g grasa"),
        
        ("", ""),
        ("🥕 VERDURAS", ""),
        ("Tomate", "18 kcal, 0.9g proteína, 3.9g carb, 0.2g grasa"),
        ("Cebolla", "40 kcal, 1.1g proteína, 9.3g carb, 0.1g grasa"),
        ("Zanahoria", "41 kcal, 0.9g proteína, 9.6g carb, 0.2g grasa"),
        ("Lechuga", "15 kcal, 1.4g proteína, 2.9g carb, 0.2g grasa"),
        
        ("", ""),
        ("🍎 FRUTAS", ""),
        ("Manzana", "52 kcal, 0.3g proteína, 14g carb, 0.2g grasa"),
        ("Plátano", "89 kcal, 1.1g proteína, 23g carb, 0.3g grasa"),
        ("Naranja", "47 kcal, 0.9g proteína, 12g carb, 0.1g grasa"),
        
        ("", ""),
        ("🥜 GRASAS Y ACEITES", ""),
        ("Aceite de oliva (1 cucharada)", "119 kcal, 0g proteína, 0g carb, 13.5g grasa"),
        ("Mantequilla (1 cucharada)", "102 kcal, 0.1g proteína, 0g carb, 11.5g grasa"),
        ("Aguacate", "160 kcal, 2g proteína, 9g carb, 15g grasa"),
    ]
    
    for alimento, info in alimentos_referencia:
        if info == "":
            print()
        elif alimento.startswith(("🥩", "🥛", "🥖", "🥕", "🍎", "🥜")):
            print(f"\n{alimento}")
            print("-" * 40)
        else:
            print(f"  • {alimento:<25} → {info}")
    
    print("\n💡 CONSEJOS:")
    print("  • Estos valores son aproximados y pueden variar según la marca")
    print("  • Para mayor precisión, consulta las etiquetas nutricionales")
    print("  • 1 gramo de carbohidratos = 4 kcal")
    print("  • 1 gramo de proteína = 4 kcal") 
    print("  • 1 gramo de grasa = 9 kcal")
    print()

def menu_principal():
    """Menú principal del programa"""
    base_datos = BaseDatosIngredientes()
    calculadora = CalculadoraRecetas(base_datos)
    
    mostrar_titulo()
    
    while True:
        print("\n📋 MENÚ PRINCIPAL")
        print("1. 📦 Registrar ingredientes/productos")
        print("2. 📋 Ver ingredientes registrados")
        print("3. 🍳 Crear y calcular receta")
        print("4. 🥗 Ver tabla de calorías de referencia")
        print("5. ❌ Salir")
        
        opcion = input("\nSelecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            registrar_ingredientes(base_datos)
        elif opcion == "2":
            base_datos.listar_ingredientes()
        elif opcion == "3":
            crear_receta(base_datos, calculadora)
        elif opcion == "4":
            mostrar_tabla_calorias()
        elif opcion == "5":
            print("\n👋 ¡Gracias por usar el Sistema de Gestión de Recetas!")
            print("¡Que tengas un excelente día!")
            break
        else:
            print("❌ Opción inválida. Selecciona 1, 2, 3, 4 o 5.")

if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido por el usuario. ¡Hasta luego!")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        print("Por favor, reinicia el programa.")