from abc import ABC
from typing import Optional, List

from astronomical_simulation_backend.domain.celestial_body import CelestialBody


class ICelestialBodyRepository(ABC):
    def get(self, entry_id: str) -> CelestialBody:
        ...

    def add(self, entry: CelestialBody) -> None:
        ...

    def get_all(self, search: Optional[str]) -> List[CelestialBody]:
        ...
