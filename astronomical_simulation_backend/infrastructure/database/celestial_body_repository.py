import os
import pickle
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Dict

from astronomical_simulation_backend.domain.celestial_body import CelestialBody
from astronomical_simulation_backend.domain.celestial_body_repository import (
    ICelestialBodyRepository,
)


class CelestialBodyNotFound(Exception):
    pass


class EntryIdNotIncluded(Exception):
    pass


@dataclass
class CelestialBodyPickleRepository(ICelestialBodyRepository):
    storage_dir: str

    def get(self, entry_id: str) -> CelestialBody:
        try:
            entry: CelestialBody
            with open(Path(self.storage_dir + "/celestial_bodies") / entry_id, mode="rb") as entry_file:
                entry = pickle.load(entry_file)
            return entry
        except Exception:
            raise CelestialBodyNotFound()

    def add(self, entry: CelestialBody) -> None:
        with open(Path(self.storage_dir + "/celestial_bodies") / entry.id, mode="wb") as entry_file:
            pickle.dump(entry, entry_file)

    def remove(self, entry_id: str) -> None:
        os.remove(Path(self.storage_dir + "/celestial_bodies") / entry_id)

    def edit(self, content: Dict[str, str]) -> None:
        try:
            entry_id = content["id"]
        except Exception:
            raise EntryIdNotIncluded()
        with open(Path(self.storage_dir + "/celestial_bodies") / entry_id, mode="rb") as entry_file:
            entry: CelestialBody = pickle.load(entry_file)
        entry.update_from_content(content)
        with open(Path(self.storage_dir + "/celestial_bodies") / entry_id, mode="wb") as entry_file:
            pickle.dump(entry, entry_file)

    def get_all(self, search: Optional[str]) -> List[CelestialBody]:
        entries: List[CelestialBody] = []
        for entry_file_path in Path(self.storage_dir + "/celestial_bodies").iterdir():
            with open(entry_file_path, mode="rb") as entry_file:
                entry: CelestialBody = pickle.load(entry_file)
                if search:
                    if search in entry.simulation_id:
                        entries.append(entry)
                else:
                    entries.append(entry)
        return entries
