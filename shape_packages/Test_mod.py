from shape_mod import Point, Line, Square, Isosceles


square_points = [Point(1,1), Point(4,1), Point(4,4), Point(1,4)]
square_lines = [
    Line(square_points[0], square_points[1]),
    Line(square_points[1], square_points[2]),
    Line(square_points[2], square_points[3]),
    Line(square_points[3], square_points[0])
]
square = Square(square_points, square_lines)
print("\nSquare Object:")
print(square)

iso_points = [Point(0, 0), Point(2, 0), Point(1, 2)]
iso_lines = [
    Line(iso_points[0], iso_points[1]),
    Line(iso_points[1], iso_points[2]),
    Line(iso_points[2], iso_points[0])
]
isosceles = Isosceles(iso_points, iso_lines)
print("\nIsosceles Object:")
print(isosceles)