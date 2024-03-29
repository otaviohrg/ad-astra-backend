from dataclasses import dataclass
from typing import Dict, List, Optional

from astronomical_simulation_backend.domain.celestial_body import CelestialBody
from astronomical_simulation_backend.domain.celestial_body_repository import (
    ICelestialBodyRepository,
)


@dataclass
class CelestialBodyService:
    celestial_body_repository: ICelestialBodyRepository

    def add_entry(self, content: Dict[str, str]) -> str:
        entry = CelestialBody.create_from_content(content)
        self.celestial_body_repository.add(entry)
        return entry.id

    def remove_entry(self, entry_id: str) -> None:
        self.celestial_body_repository.remove(entry_id)

    def edit_entry(self, content: Dict[str, str]):
        self.celestial_body_repository.edit(content)

    def add_position_to_trajectory(self, entry_id: str) -> None:
        self.celestial_body_repository.get(entry_id).add_position_to_trajectory()

    def get_all(self, search: Optional[str] = None) -> List[CelestialBody]:
        return self.celestial_body_repository.get_all(search)
