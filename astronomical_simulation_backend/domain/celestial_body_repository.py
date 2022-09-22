from abc import ABC
from typing import List, Optional

from astronomical_simulation_backend.domain.celestial_body import CelestialBody


class ICelestialBodyRepository(ABC):
    def get(self, entry_id: str) -> CelestialBody:
        ...

    def add(self, entry: CelestialBody) -> None:
        ...

    def remove(self, entry_id: str) -> None:
        ...

    def edit(self, entry_id: str) -> None:
        ...

    def get_all(self, search: Optional[str]) -> List[CelestialBody]:
        ...
