# Implementaciones de Patrones de Diseño

Esta carpeta contiene las implementaciones en Python de los 5 patrones de diseño aplicados al sistema de gestión de empleados.

## 🏗️ Patrones Implementados

### Creacionales
- **`builder/`** - Patrón Builder para construcción flexible de objetos Employee
- **`factory_method/`** - Patrón Factory Method para creación de roles de empleados

### Comportamiento
- **`strategy/`** - Patrón Strategy para algoritmos de cálculo salarial intercambiables
- **`observer/`** - Patrón Observer para notificaciones automáticas del sistema

### Estructural
- **`adapter/`** - Patrón Adapter para integración con sistemas legacy y APIs externas

## 📂 Estructura de Cada Patrón

Cada subcarpeta contiene:
- **`[patron].py`** - Implementación completa del patrón en Python
- **`[patron]_diagram.puml`** - Diagrama UML en formato PlantUML

## 🚀 Cómo Ejecutar

Para ejecutar cualquier patrón:

```bash
cd src/[nombre_del_patron]
python [nombre_del_patron].py
```

### Ejemplos:
```bash
cd src/builder
python builder.py

cd src/observer
python observer.py
```

## 📋 Descripción de Patrones

### Builder Pattern
Construye objetos complejos paso a paso, permitiendo diferentes representaciones del mismo objeto.

### Factory Method Pattern
Define una interfaz para crear objetos, permitiendo que subclases decidan qué clase instanciar.

### Strategy Pattern
Encapsula algoritmos intercambiables y los hace seleccionables en tiempo de ejecución.

### Observer Pattern
Define dependencia uno-a-muchos entre objetos para notificaciones automáticas.

### Adapter Pattern
Permite que interfaces incompatibles trabajen juntas mediante un adaptador.

## 🎯 Propósito Educativo

Cada implementación incluye:
- Código limpio y bien comentado
- Ejemplos de uso prácticos
- Demostración de beneficios del patrón
- Casos de uso aplicados al dominio de empleados