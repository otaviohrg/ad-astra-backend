import uuid
import math
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Tuple
from astronomical_simulation_backend.domain.constants import SAMPLE_TIME


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
    simulation_id: str

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
            simulation_id=content["simulation_id"]
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

    def add_position_to_trajectory(self) -> None:
        self.position_list.append((self.x_coordinate, self.y_coordinate))

    def compute_attraction(self, other: 'CelestialBody', degree: float, k: float):

        if self is other:
            raise ValueError("Attraction of object %r to itself requested"
                             % self.name)

        # Compute the distance of the other body.
        sx, sy = self.x_coordinate, self.y_coordinate
        ox, oy = other.x_coordinate, other.y_coordinate
        dx = (ox - sx)
        dy = (oy - sy)
        d = math.sqrt(dx ** 2 + dy ** 2)

        # Stop in case of collision, considered as perfectly inelastic
        if d <= self.radius + other.radius:
            self.collide(other)
            return 0.0, 0.0

        # Compute the force of attraction
        f = k * self.mass * other.mass / (d ** degree)

        # Compute the direction of the force.
        theta = math.atan2(dy, dx)
        fx = math.cos(theta) * f
        fy = math.sin(theta) * f
        return fx, fy

    def collide(self, other: 'CelestialBody') -> None:
        v_res_x = (self.mass * self.x_speed + other.mass * other.x_speed)/(self.mass+other.mass)
        v_res_y = (self.mass * self.y_speed + other.mass * other.y_speed) / (self.mass + other.mass)

        self.x_speed = other.x_speed = v_res_x
        self.y_speed = other.y_speed = v_res_y

    def result_force(self, bodies: List['CelestialBody'], degree: float, k: float):
        total_fx = total_fy = 0.0
        for other in bodies:
            # Don't calculate the body's attraction to itself
            if self is other:
                continue
            fx, fy = self.compute_attraction(other, degree, k)
            total_fx += fx
            total_fy += fy
        # Record the total force exerted.
        return total_fx, total_fy

    def set_velocity(self, bodies, deg, k):
        dt = SAMPLE_TIME
        fx, fy = self.result_force(bodies, deg, k)
        self.x_speed += fx / self.mass * dt
        self.y_speed += fy / self.mass * dt

    def move(self):
        dt = SAMPLE_TIME
        self.x_coordinate += self.x_speed * dt
        self.y_coordinate += self.x_speed * dt
