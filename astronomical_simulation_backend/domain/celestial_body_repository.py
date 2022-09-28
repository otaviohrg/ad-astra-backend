from abc import ABC
from typing import Dict, List, Optional

from astronomical_simulation_backend.domain.celestial_body import CelestialBody


class ICelestialBodyRepository(ABC):
    def get(self, entry_id: str) -> CelestialBody:
        ...

    def add(self, entry: CelestialBody) -> None:
        ...

    def remove(self, entry_id: str) -> None:
        ...

    def edit(self, entry: Dict[str, str]) -> None:
        ...

    def update_from_object(self, entry: CelestialBody) -> None:
        ...

    def get_all(self, search: Optional[str]) -> List[CelestialBody]:
        ...
