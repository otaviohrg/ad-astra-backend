from abc import ABC
from typing import Dict

from astronomical_simulation_backend.domain.simulation import Simulation


class ISimulationRepository(ABC):
    def get(self, simulation_id: str) -> Simulation:
        ...

    def create(self, entry: Simulation) -> None:
        ...

    def remove(self, simulation_id: str) -> None:
        ...

    def edit(self, content: Dict[str, str]) -> None:
        ...

    def run(self, simulation_id: str) -> Simulation:
        ...

    def add_body(self, body_id: str) -> None:
        ...
