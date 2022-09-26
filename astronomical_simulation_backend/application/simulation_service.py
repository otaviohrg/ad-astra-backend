from dataclasses import dataclass
from typing import Dict, Optional

from astronomical_simulation_backend.domain.simulation import Simulation
from astronomical_simulation_backend.domain.simulation_repository import (
    ISimulationRepository,
)


@dataclass
class SimulationService:
    simulation_repository: ISimulationRepository

    def add_simulation(self, content: Dict[str, str]) -> str:
        entry = Simulation.create_system(content)
        self.simulation_repository.create(entry)
        return entry.id

    def remove_entry(self, simulation_id: str) -> None:
        self.simulation_repository.remove(simulation_id)

    def edit_entry(self, content: Dict[str, str]):
        self.simulation_repository.edit(content)
