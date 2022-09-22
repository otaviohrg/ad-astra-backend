from typing import List, Tuple

from pydantic import BaseModel


class CelestialBodySchema(BaseModel):
    id: str
    name: str
    mass: float
    angular_speed: float
    x_coordinate: float
    y_coordinate: float
    x_speed: float
    y_speed: float
    radius: float
    position_list: List[Tuple[float, float]]
