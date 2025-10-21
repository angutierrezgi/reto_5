# reto_5
This repository refers to the activities proposed for class 11 of the Object Oriented Pogramming course.
___

Se ha implementado como requerido, la implementación de dos paquetes para construir los elementos derivados de la clase *Shape*, que se pueden hallar de la siguiente manera:

```markdown
Shape_packages/
│
├── shape_mod/
│   ├── __init__.py
│   ├── line.py
│   ├── point.py
│   ├── rectangle.py
│   ├── shape.py
│   └── triangle.py
│
├── shape_unique/
│   ├── __init__.py
│   └── shape.py
│
├── Test_mod.py
└── Test_unique.py
```
___
### shape_mod
Aquí se estructura el paquete por medio de diferentes módulos, en el cual cada uno contiene su clase respectiva, o clases derivadas que contienen la funcionalidad del código original:

```markdown
shape_mod/
│
├── __init__.py        # Initializador del paquete, contiene todos los imports
├── line.py            # Contiene la clase Line
├── point.py           # Contiene la clase Point
├── rectangle.py       # Contiene la clase Rectangle y Square
├── shape.py           # Contiene la clase abstracta Shape
└── triangle.py        # Contiene la clase Triangle y sus subclases
```
```python
# __init__.py
from .point import Point
from .line import Line
from .shape  import Shape
from .rectangle import Rectangle, Square
from .triangle import Triangle, Equilateral, Isosceles, Scalene, TriRectangle

__all__ = [
    "Point", "Line", "Shape",
    "Rectangle", "Square",
    "Triangle", "Equilateral", "Isosceles", "Scalene", "TriRectangle"
]
```
___
### shape_unique
Aquí se estructura el paquete a través de un solo módulo que contiene todo el código, y el initializador únicamente:
```markdown
shape_unique/
│
├── __init__.py     # Importa todo el contenido de shape
└── shape.py        # Contiene todo la estructura de clases
```
```python
# __init__.py
from .shape import Point, Line, Shape, Rectangle, Square, Triangle, Equilateral, Isosceles, Scalene, TriRectangle

__all__ = [
    "Point", "Line", "Shape",
    "Rectangle", "Square",
    "Triangle", "Equilateral", "Isosceles", "Scalene", "TriRectangle"
]
```

