import uuid
from datetime import datetime
from dataclasses import dataclass, field

from typing import List, Set, Tuple


@dataclass
class CelestialBody:
    id: str
    created_at: datetime
    name: str
    mass: float
    angular_speed: float
    x_coordinate: float
    y_coordinate: float
    x_speed: float
    y_speed: float
    radius: float
    position_list: List[Tuple[float, float]]

    @classmethod
    def create_from_content(cls,
                            name: str,
                            mass: float,
                            angular_speed: float,
                            x_coordinate: float,
                            y_coordinate: float,
                            x_speed: float,
                            y_speed: float,
                            radius: float) -> "CelestialBody":
        return cls(id=str(uuid.uuid4()),
                   created_at=datetime.utcnow(),
                   name=name,
                   mass=mass,
                   angular_speed=angular_speed,
                   x_coordinate=x_coordinate,
                   y_coordinate=y_coordinate,
                   x_speed=x_speed,
                   y_speed=y_speed,
                   radius=radius,
                   position_list=[])

    def add_point_to_trajectory(self, point: Tuple[float, float]) -> None:
        self.position_list.append(point)
