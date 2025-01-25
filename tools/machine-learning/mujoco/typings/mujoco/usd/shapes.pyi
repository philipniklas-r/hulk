import mujoco
import numpy as np
from _typeshed import Incomplete
from typing import Any

def get_triangle_uvs(vertices: np.ndarray, triangles: np.ndarray, texture_type: mujoco.mjtTexture | None): ...

class TriangleMesh:
    vertices: Incomplete
    triangles: Incomplete
    triangle_uvs: Incomplete
    def __init__(self, vertices: np.ndarray, triangles: np.ndarray, triangle_uvs: np.ndarray) -> None: ...
    @classmethod
    def create_box(cls, width: float, height: float, depth: float, texture_type: mujoco.mjtTexture | None) -> TriangleMesh: ...
    @classmethod
    def create_sphere(cls, radius: float, texture_type: mujoco.mjtTexture | None, resolution: int) -> TriangleMesh: ...
    @classmethod
    def create_hemisphere(cls, radius: float, texture_type: mujoco.mjtTexture | None, resolution: int) -> TriangleMesh: ...
    @classmethod
    def create_cylinder(cls, radius: float, height: float, texture_type: mujoco.mjtTexture | None, resolution: int) -> TriangleMesh: ...
    def translate(self, translation: np.ndarray) -> None: ...
    def rotate(self, rotation: np.ndarray, center: tuple[float, ...]) -> None: ...
    def scale(self, scale: np.ndarray) -> None: ...
    def get_center(self): ...
    def __add__(self, other): ...

def decouple_config(config: dict[str, Any]): ...
def mesh_config_generator(name: str, geom_type: int | mujoco.mjtGeom, size: np.ndarray, decouple: bool = False): ...
def mesh_factory(mesh_config: dict[str, Any], texture_type: mujoco.mjtTexture | None, resolution: int = 100): ...
