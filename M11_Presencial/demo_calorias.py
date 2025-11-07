#!/Users/enriquegarcia/Desktop/Repositories CS1400/.venv/bin/python

# Demo automática del Sistema de Gestión de Recetas con Calorías

import os
import sys
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

try:
    from tabulate import tabulate
    _TABULATE = True
except ImportError:
    _TABULATE = False

# Importar solo las clases necesarias
from PROGRAMA_COMPLETO import Ingrediente, BaseDatosIngredientes, LineaReceta, CalculadoraRecetas, mostrar_resultado_receta

def demo_completa():
    print("🎬 DEMO AUTOMÁTICA - Sistema de Recetas con Calorías")
    print("="*60)
    
    # Crear base de datos
    base_datos = BaseDatosIngredientes()
    calculadora = CalculadoraRecetas(base_datos)
    
    # Registrar ingredientes con información nutricional
    print("\n📦 Registrando ingredientes con información nutricional...")
    
    ingredientes_ejemplo = [
        Ingrediente("H001", "Harina de trigo", "Panadería", "Marca A", "Proveedor 1", 
                   1, "kg", 2.50, 364, 10, 76, 1),
        Ingrediente("H002", "Huevos", "Lácteos", "Frescos", "Granja Local", 
                   12, "pcs", 3.00, 70, 6, 1, 5),
        Ingrediente("A001", "Azúcar", "Panadería", "Blanca", "Proveedor 1", 
                   1, "kg", 1.80, 387, 0, 100, 0),
        Ingrediente("L001", "Leche entera", "Lácteos", "Fresca", "Lechería", 
                   1, "litro", 2.20, 61, 3.2, 4.5, 3.25),
        Ingrediente("M001", "Mantequilla", "Lácteos", "Sin sal", "Lechería", 
                   500, "g", 8.50, 7.17, 0.9, 0.1, 0.81)  # 717 cal/100g = 7.17 cal/g
    ]
    
    for ing in ingredientes_ejemplo:
        base_datos.agregar_ingrediente(ing)
        print(f"✅ {ing.nombre} - {ing.calorias_por_unidad} kcal por {ing.unidad}")
    
    # Crear una receta de ejemplo
    print("\n🍳 Creando receta: Torta básica...")
    
    receta_torta = [
        LineaReceta("Harina de trigo", 0.5, "kg"),
        LineaReceta("Huevos", 3, "pcs"),
        LineaReceta("Azúcar", 0.3, "kg"),
        LineaReceta("Leche entera", 0.25, "litro"),
        LineaReceta("Mantequilla", 200, "g")
    ]
    
    # Calcular la receta
    resultado = calculadora.calcular_receta(
        receta_torta, 
        porciones=8, 
        objetivo_costo_comida_pct=25, 
        precio_menu_actual=15.99
    )
    
    # Mostrar resultados
    mostrar_resultado_receta(resultado)

if __name__ == "__main__":
    demo_completa()