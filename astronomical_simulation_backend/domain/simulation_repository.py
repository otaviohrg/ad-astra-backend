from abc import ABC
from typing import Dict, Optional, List

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

    def get_all(self) -> List[Simulation]:
        ...
