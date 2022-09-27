import os
import pickle
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict

from astronomical_simulation_backend.domain.simulation import Simulation
from astronomical_simulation_backend.domain.simulation_repository import (
    ISimulationRepository,
)


class SimulationNotFound(Exception):
    pass


class SimulationIdNotIncluded(Exception):
    pass


@dataclass
class SimulationPickleRepository(ISimulationRepository):
    storage_dir: str

    def get(self, simulation_id: str) -> Simulation:
        try:
            simulation: Simulation
            with open(Path(self.storage_dir + "/simulation") / simulation_id, mode="rb") as entry_file:
                simulation = pickle.load(entry_file)
            return simulation
        except Exception:
            raise SimulationNotFound()

    def create(self, simulation: Simulation) -> None:
        with open(Path(self.storage_dir + "/simulation") / simulation.id, mode="wb") as entry_file:
            pickle.dump(simulation, entry_file)

    def remove(self, simulation_id: str) -> None:
        os.remove(Path(self.storage_dir + "/simulation") / simulation_id)

    def edit(self, content: Dict[str, str]) -> None:
        try:
            simulation_id = content["id"]
        except Exception:
            raise SimulationIdNotIncluded()
        with open(Path(self.storage_dir + "/simulation") / simulation_id, mode="rb") as entry_file:
            simulation: Simulation = pickle.load(entry_file)
        simulation.update_from_content(content)
        with open(Path(self.storage_dir + "/simulation") / simulation_id, mode="wb") as entry_file:
            pickle.dump(simulation, entry_file)

    def get_all(self) -> List[Simulation]:
        simulations: List[Simulation] = []
        for simulation_file_path in Path(self.storage_dir + "/simulation").iterdir():
            with open(simulation_file_path, mode="rb") as entry_file:
                entry: Simulation = pickle.load(entry_file)
                simulations.append(entry)
        return simulations
