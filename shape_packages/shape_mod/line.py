from .point import Point

class Line():
    def __init__(self, start_point: Point, end_point: Point):
        self._start: Point = start_point
        self._end: Point = end_point
        self._length: float = start_point.compute_distance(end_point)
        self._slope: float = self.compute_slope()

    @property
    def start(self):
        return self._start
    @property
    def y(self):
        return self._y
    
    def compute_length(self) -> float:
        return self._length
    def compute_slope(self) -> float:
        slope: float = None
        if self._end.x - self._start.x == 0:
            slope = None
            return slope
        else:
            slope = (self._end.y - self._start.y) / (self._end.x - self._start.x)
            return round(slope, 3)
    def compute_horizontal_cross(self) -> bool:
        x_intersect: bool = False
        if self._start.y >= 0 and self._end.y <= 0:
            x_intersect = True
        elif self._start.y <= 0 and self._end.y >= 0:
            x_intersect = True
        return x_intersect
    def compute_vertical_cross(self) -> bool:
        y_intersect: bool = False
        if self._start.x >= 0 and self._end.x <= 0:
            y_intersect = True
        elif self._start.x <= 0 and self._end.x >= 0:
            y_intersect = True
        return y_intersect
    def discretize_line(self, n : int) -> list:
        i: int = 0
        points: list = []
        while(i < n):
            aux_x = self._start.x + ((i / (n - 1)) * (self._end.x - self._start.x))
            aux_y = self._start.y + ((i / (n - 1)) * (self._end.y - self._start.y))
            points.append(Point(round(aux_x, 3),round(aux_y, 3)))
            i += 1
        return points
    def __str__(self):
        result: list = [
            f"Start: {self._start}",
            f"End: {self._end}",
            f"Length: {self.compute_length()}",
            f"Slope: {self.compute_slope()}",
            f"Cross x-axis: {self.compute_horizontal_cross()}",
            f"Cross y-axis: {self.compute_vertical_cross()}"
        ]
        return "\n".join(result)
