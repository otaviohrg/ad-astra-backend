import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict

from astronomical_simulation_backend.domain.celestial_body import CelestialBody


@dataclass
class Simulation:
    id: str
    created_at: datetime
    k: float
    degree: float
    status: str
    celestial_bodies: List[CelestialBody]

    @classmethod
    def create_system(cls, params: Dict[str, str]) -> "Simulation":
        return cls(
            id=str(uuid.uuid4()),
            created_at=datetime.utcnow(),
            k=float(params["k"]),
            degree=float(params["degree"]),
            status="STOPPED",
            celestial_bodies=[],
        )

    def add_celestial_body(self, celestial_body: CelestialBody):
        self.celestial_bodies.append(celestial_body)

    def update(self):
        for body in self.celestial_bodies:
            body.set_velocity(self.celestial_bodies, self.degree, self.k)
            body.move()
    