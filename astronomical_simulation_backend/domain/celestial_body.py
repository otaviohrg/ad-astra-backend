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

    def update_from_content(self, content: Dict[str, str]) -> None:
        for key in content.keys():
            if key == "name":
                self.name = content[key]
            if key == "mass":
                self.mass = float(content[key])
            if key == "x_coordinate":
                self.x_coordinate = float(content[key])
            if key == "y_coordinate":
                self.y_coordinate = float(content[key])
            if key == "x_speed":
                self.x_speed = float(content[key])
            if key == "y_speed":
                self.y_speed = float(content[key])
            if key == "radius":
                self.radius = float(content[key])

    def add_point_to_trajectory(self, point: Tuple[float, float]) -> None:
        self.position_list.append(point)
