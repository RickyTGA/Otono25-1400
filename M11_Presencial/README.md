# 🍽️ Sistema de Gestión de Recetas con Análisis Nutricional

## 📋 Descripción
Sistema completo para negocios de comida que permite calcular costos de recetas, analizar rentabilidad y obtener información nutricional detallada incluyendo calorías, proteínas, carbohidratos y grasas.

## ✨ Funcionalidades Principales

### 💰 Gestión Financiera
- ✅ Cálculo automático de costos por ingrediente
- ✅ Análisis de rentabilidad por porción
- ✅ Recomendaciones de precios basadas en objetivos de costo
- ✅ Comparación entre precios objetivo vs. actuales

### 🥗 Análisis Nutricional
- 🔥 **Cálculo de calorías** por ingrediente y receta completa
- 🥩 **Análisis de proteínas** (gramos por porción)
- 🍞 **Análisis de carbohidratos** (gramos por porción)
- 🧈 **Análisis de grasas** (gramos por porción)
- 📊 **Clasificación automática** de calorías:
  - 🟢 Bajo: < 200 kcal
  - 🟡 Moderado: 200-400 kcal
  - 🟠 Alto: 400-600 kcal
  - 🔴 Muy alto: > 600 kcal

### 📚 Herramientas Adicionales
- 📋 **Tabla de referencia nutricional** con alimentos comunes
- 💡 **Consejos nutricionales** y conversiones calóricas
- 🎲 **Demo automática** con ejemplos prácticos
- 📊 **Reportes detallados** en formato tabla

## 🚀 Cómo Usar

### 1. Ejecutar el Programa Principal
```bash
python PROGRAMA_COMPLETO.py
```

### 2. Flujo de Trabajo
1. **📦 Registrar Ingredientes**: Agrega productos con información de costo y nutricional
2. **🍳 Crear Recetas**: Define ingredientes y cantidades
3. **📊 Analizar Resultados**: Obtén costos, precios recomendados e información nutricional
4. **🥗 Consultar Tabla de Calorías**: Usa la referencia nutricional integrada

### 3. Demo Automática
```bash
python demo_calorias.py
```
Ejecuta una demostración con una receta de torta básica que muestra todas las funcionalidades.

## 📊 Ejemplo de Salida

### Receta: Torta Básica (8 porciones)
```
📦 INGREDIENTES:
| Ingrediente     | Cantidad | Unidad | Costo   | Calorías    |
|-----------------|----------|--------|---------|-------------|
| Harina de trigo | 0.5      | kg     | $1.25   | 182.0 kcal  |
| Huevos          | 3        | pcs    | $0.75   | 210.0 kcal  |
| Azúcar          | 0.3      | kg     | $0.54   | 116.1 kcal  |
| Mantequilla     | 200      | g      | $3.40   | 1434.0 kcal |

💰 RESUMEN FINANCIERO:
   Costo por porción: $0.81
   Precio objetivo recomendado: $3.25

🥗 INFORMACIÓN NUTRICIONAL:
   Por porción: 244.7 kcal
   Proteínas: 25.5g | Carbohidratos: 11.5g | Grasas: 22.3g
   📊 Clasificación: 🟡 Moderado en calorías
```

## 📁 Archivos Incluidos

- **`PROGRAMA_COMPLETO.py`**: Sistema principal interactivo
- **`demo_calorias.py`**: Demostración automática
- **`ingredients_example.csv/xlsx`**: Datos de prueba
- **`recipe_example.csv`**: Receta de ejemplo
- **`m11_rectangulo_ej1.py`**: Ejercicio de clases (Rectangle)

## 🎯 Casos de Uso

### Para Restaurantes
- ✅ Cumplir con regulaciones de etiquetado nutricional
- ✅ Optimizar costos manteniendo calidad nutricional
- ✅ Ofrecer opciones saludables con datos precisos

### Para Negocios de Comida Saludable
- ✅ Marketing basado en información nutricional
- ✅ Desarrollo de menús balanceados
- ✅ Control de calorías por porción

### Para Análisis de Costos
- ✅ Establecer precios competitivos
- ✅ Analizar rentabilidad por producto
- ✅ Identificar ingredientes costosos vs. valor nutricional

## 🔧 Instalación

### Requisitos
```bash
pip install pandas tabulate openpyxl
```

### Configuración del Entorno Python
El programa incluye configuración automática del entorno virtual para asegurar compatibilidad.

## 📈 Nuevas Funcionalidades vs. Versión Anterior

| Característica | Versión Anterior | Nueva Versión |
|----------------|------------------|---------------|
| Cálculo de costos | ✅ | ✅ |
| Análisis de rentabilidad | ✅ | ✅ |
| **Calorías por ingrediente** | ❌ | ✅ |
| **Análisis de macronutrientes** | ❌ | ✅ |
| **Clasificación nutricional** | ❌ | ✅ |
| **Tabla de referencia** | ❌ | ✅ |
| **Demo automática** | ❌ | ✅ |
| Interfaz user-friendly | ⚠️ Básica | ✅ Completa |

## 🏆 Ventajas Competitivas

1. **📊 Información Dual**: Combina análisis financiero y nutricional
2. **🎯 Clasificación Automática**: Identifica productos por nivel calórico
3. **📚 Referencia Integrada**: No necesitas buscar calorías en otras fuentes
4. **🚀 Fácil de Usar**: Interfaz guiada paso a paso
5. **📈 Escalable**: Desde pequeños negocios hasta cadenas de restaurantes

---

## 💡 Desarrollado para el Curso CS1400
**Módulo 11**: Programación Orientada a Objetos y Aplicaciones Prácticas

**Características Técnicas**:
- ✅ Uso de clases y objetos (`@dataclass`)
- ✅ Manejo de archivos CSV/Excel
- ✅ Interfaces de usuario interactivas
- ✅ Cálculos matemáticos precisos
- ✅ Formateo de datos con `tabulate`
- ✅ Gestión de errores y validaciones

---
**🔗 Repositorio**: [CS1400 - Otoño 2025](https://github.com/RickyTGA/Otono25-1400)
**📧 Contacto**: Proyecto académico CS1400