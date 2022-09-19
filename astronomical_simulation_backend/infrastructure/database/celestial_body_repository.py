import pickle
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, List

from astronomical_simulation_backend.domain.celestial_body import CelestialBody
from astronomical_simulation_backend.domain.celestial_body_repository import ICelestialBodyRepository


class CelestialBodyNotFound(Exception):
    pass


@dataclass
class CelestialBodyPickleRepository(ICelestialBodyRepository):
    storage_dir: str

    def get(self, entry_id: str) -> CelestialBody:
        try:
            entry: CelestialBody
            with open(Path(self.storage_dir) / entry_id) as entry_file:
                entry = pickle.load(entry_file)
            return entry
        except Exception:
            raise CelestialBodyNotFound()

    def add(self, entry: CelestialBody) -> None:
        with open(Path(self.storage_dir) / entry.id) as entry_file:
            pickle.dump(entry, entry_file)

    def get_all(self, search: Optional[str]) -> List[CelestialBody]:
        entries: List[CelestialBody] = []
        for entry_file_path in Path(self.storage_dir).iterdir():
            with open(entry_file_path, mode="rb") as entry_file:
                entry: CelestialBody = pickle.load(entry_file)
                if search:
                    if search in entry.name:
                        entries.append(entry)
                else:
                    entries.append(entry)
        return entries
