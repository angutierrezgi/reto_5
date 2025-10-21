import math

class Shape():
    def __init__(self, vertices: list, edges: list):
        self._vertices: list = vertices
        self._edges: list = edges
        self._inner_angles: list = self.compute_inner_angles()
        self.is_regular: bool = False
    def compute_inner_angles(self) -> list:
        angles: list = []
        n_verts = len(self._vertices)
        for i in range(n_verts):
            prev_vert = self._vertices[i - 1]
            midl_vert = self._vertices[i]
            next_vert = self._vertices[(i + 1) % n_verts]

            v = [prev_vert.x - midl_vert.x, prev_vert.y - midl_vert.y]
            u = [next_vert.x - midl_vert.x, next_vert.y - midl_vert.y]

            dot_prod = v[0] * u[0] + v[1] * u[1]
            norm_v = ((v[0] * v[0]) + (v[1] * v[1])) ** 0.5
            norm_u = ((u[0] * u[0]) + (u[1] * u[1])) ** 0.5

            cos_angle = dot_prod / (norm_u * norm_v)
            cos_angle = max(-1.0, min(1.0, cos_angle))
            angle_rad = math.acos(cos_angle)
            angle_deg = math.degrees(angle_rad)

            angles.append(round(angle_deg, 3))
        return angles
    def compute_area():
        raise NotImplementedError("Must be implemented in subclass!!")
    def compute_perimeter():
        raise NotImplementedError("Must be implemented in subclass!!")
