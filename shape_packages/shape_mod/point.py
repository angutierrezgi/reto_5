class Point():
    definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."
    def __init__(self, x: float=0, y: float=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, new_x):
        self._x = new_x

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, new_y):
        self._y = new_y
    
    def reset(self):
        self.x = 0
        self.y = 0
    def compute_distance(self, point: "Point")-> float:
        distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
        return distance
    def __repr__(self):
        return f"({self.x},{self.y})"