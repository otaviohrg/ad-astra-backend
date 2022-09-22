import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Tuple


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
    def create_from_content(cls, content: Dict[str, str]) -> "CelestialBody":
        return cls(
            id=str(uuid.uuid4()),
            created_at=datetime.utcnow(),
            name=content["name"],
            mass=float(content["mass"]),
            angular_speed=float(content["angular_speed"]),
            x_coordinate=float(content["x_coordinate"]),
            y_coordinate=float(content["y_coordinate"]),
            x_speed=float(content["x_speed"]),
            y_speed=float(content["y_speed"]),
            radius=float(content["radius"]),
            position_list=[],
        )

    def add_point_to_trajectory(self, point: Tuple[float, float]) -> None:
        self.position_list.append(point)
