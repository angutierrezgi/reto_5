from .shape import Shape

class Rectangle(Shape):
    def __init__(self, vertices: list, edges: list):
        super().__init__(vertices, edges)
        self.width: float = self._edges[0].compute_length()
        self.height: float = self._edges[1].compute_length()
        if self.width == self.height:
            self.is_regular: bool = True
        else:
            self.is_regular: bool = False
    def compute_area(self) -> float:
        return self.width * self.height
    def compute_perimeter(self) -> float:
        return 2*self.width + 2*self.height
    def __str__(self):
        result: list = [
            f"Vertices: {self._vertices}",
            f"Inner Angles: {self._inner_angles}",
            f"Width: {self.width}",
            f"Height: {self.height}",
            f"Regular Shape: {self.is_regular}",
            f"Area: {self.compute_area()}",
            f"Perimeter: {self.compute_perimeter()}"
        ]
        return "\n".join(result)  
      
class Square(Rectangle):
    def __init__(self, vertices: list, edges: list):
        super().__init__(vertices, edges)
        if not (self._edges[0].compute_length() == self._edges[1].compute_length()):
            raise ValueError("Not a Square")
        self.side_length: float = self._edges[0].compute_length()
        self.is_regular: bool = True
    def compute_area(self) -> float:
        return self.side_length ** 2
    def compute_perimeter(self) -> float:
        return 4 * self.side_length
    def __str__(self):
        result: list = [
            f"Vertices: {self._vertices}",
            f"Inner Angles: {self._inner_angles}",
            f"Side Length: {self.side_length}",
            f"Regular Shape: {self.is_regular}",
            f"Area: {self.compute_area()}",
            f"Perimeter: {self.compute_perimeter()}"
        ]
        return "\n".join(result)  
