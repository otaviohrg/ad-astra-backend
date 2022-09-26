import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict
from astronomical_simulation_backend.domain.constants import SAMPLE_TIME

from astronomical_simulation_backend.domain.celestial_body import CelestialBody


@dataclass
class Simulation:
    id: str
    created_at: datetime
    k: float
    degree: float
    status: str

    @classmethod
    def create_system(cls, params: Dict[str, str]) -> "Simulation":
        return cls(
            id=str(uuid.uuid4()),
            created_at=datetime.utcnow(),
            k=float(params["k"]),
            degree=float(params["degree"]),
            status="STOPPED"
        )

    def update(self, celestial_bodies: List[CelestialBody]) -> None:
        for body in celestial_bodies:
            body.set_velocity(celestial_bodies, self.degree, self.k)
            body.move()

    def run(self, celestial_bodies: List[CelestialBody], duration: float) -> List[CelestialBody]:
        t = 0.0
        while t < duration:
            self.update(celestial_bodies)
            for body in celestial_bodies:
                body.add_position_to_trajectory()
            t += SAMPLE_TIME
        return celestial_bodies
