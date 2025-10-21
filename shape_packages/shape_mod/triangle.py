import math
from .shape import Shape
   
class Triangle(Shape):
    def __init__(self, vertices: list, edges: list):
        super().__init__(vertices, edges)
        self._a: float = self._edges[0].compute_length()
        self._b: float = self._edges[1].compute_length()
        self._c: float = self._edges[2].compute_length()
        if math.isclose(self._a, self._b) and math.isclose(self._b, self._c):
            self.is_regular: bool = True
        else:
            self.is_regular: bool = False
    def compute_perimeter(self):
        perimeter: float = self._a + self._b + self._c
        return round(perimeter, 3)
    def compute_area(self) -> float:
        s: float = self.compute_perimeter() / 2
        area : float = (s * (s - self._a) * (s - self._b) * (s - self._c)) ** 0.5
        return round(area, 3)
    def __str__(self):
        result: list = [
            f"Vertices: {self._vertices}",
            f"Inner Angles: {self._inner_angles}",
            f"Regular Shape: {self.is_regular}",
            f"Area: {self.compute_area()}",
            f"Perimeter: {self.compute_perimeter()}"
        ]
        return "\n".join(result)  
    
class Isosceles(Triangle):
    def __init__(self, vertices: list, edges: list):
        super().__init__(vertices, edges)
        if not (math.isclose(self._a, self._b) or math.isclose(self._b, self._c) or math.isclose(self._a, self._c)):
            raise ValueError("Not an Isosceles triangle!!")
    def compute_perimeter(self):
        return super().compute_perimeter()
    def compute_area(self):
        return super().compute_area()
    def __str__(self):
        return super().__str__()
    
class Equilateral(Triangle):
    def __init__(self, vertices: list, edges: list):
        super().__init__(vertices, edges)
        self.is_regular: bool = True
        if not (math.isclose(self._a, self._b) and math.isclose(self._b, self._c)):
            raise ValueError("Not an Equilateral triangle!!")
    def compute_perimeter(self):
        return super().compute_perimeter()
    def compute_area(self):
        return super().compute_area()
    def __str__(self):
        return super().__str__()
    
class Scalene(Triangle):
    def __init__(self, vertices: list, edges: list):
        super().__init__(vertices, edges)
        if math.isclose(self._a, self._b) or math.isclose(self._b, self._c) or math.isclose(self._a, self._c):
            raise ValueError("Not an Scalene triangle!!")
    def compute_perimeter(self):
        return super().compute_perimeter()
    def compute_area(self):
        return super().compute_area()
    def __str__(self):
        return super().__str__()
    
class TriRectangle(Triangle):
    def __init__(self, vertices:list, edges: list):
        super().__init__(vertices, edges)
        if not any(math.isclose(angle, 90.0) for angle in self._inner_angles):
            raise ValueError("Not a Right Triangle!!")
    def compute_perimeter(self):
        return super().compute_perimeter()
    def compute_area(self):
        return super().compute_area()
    def __str__(self):
        return super().__str__()
