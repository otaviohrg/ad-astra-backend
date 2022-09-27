from dataclasses import dataclass
from typing import Dict, Optional, List

from astronomical_simulation_backend.domain.simulation import Simulation
from astronomical_simulation_backend.domain.celestial_body import CelestialBody
from astronomical_simulation_backend.domain.simulation_repository import (
    ISimulationRepository,
)
from astronomical_simulation_backend.domain.celestial_body_repository import (
    ICelestialBodyRepository
)
from astronomical_simulation_backend.domain.constants import SAMPLE_TIME


@dataclass
class SimulationService:
    simulation_repository: ISimulationRepository
    celestial_body_repository: ICelestialBodyRepository

    def add_simulation(self, content: Dict[str, str]) -> str:
        entry = Simulation.create_system(content)
        self.simulation_repository.create(entry)
        return entry.id

    def remove_entry(self, simulation_id: str) -> None:
        self.simulation_repository.remove(simulation_id)

    def edit_entry(self, content: Dict[str, str]) -> None:
        self.simulation_repository.edit(content)

    def get_all(self) -> List[Simulation]:
        return self.simulation_repository.get_all()

    def get_all_bodies(self, simulation_id: str) -> List[CelestialBody]:
        return self.celestial_body_repository.get_all(simulation_id)

    def run(self, duration: float, simulation_id: str) -> None:
        t = 0.0
        celestial_bodies = self.celestial_body_repository.get_all(simulation_id)
        degree, k = self.simulation_repository.get(simulation_id).get_parameters()
        self.simulation_repository.get(simulation_id).change_state("RUNNING")
        while t < duration:
            for body in celestial_bodies:
                body.set_velocity(celestial_bodies, degree, k)
                body.move()
            for body in celestial_bodies:
                body.add_position_to_trajectory()
            t += SAMPLE_TIME
        for body in celestial_bodies:
            self.celestial_body_repository.update_from_object(body)
        self.simulation_repository.get(simulation_id).change_state("STOPPED")
