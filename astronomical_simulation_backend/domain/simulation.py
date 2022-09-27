import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import Dict


@dataclass
class Simulation:
    id: str
    created_at: datetime
    k: float
    degree: float
    status: str

    @classmethod
    def create_system(cls, params: Dict[str, str]) -> "Simulation":
        return cls(
            id=str(uuid.uuid4()),
            created_at=datetime.utcnow(),
            k=float(params["k"]),
            degree=float(params["degree"]),
            status="STOPPED"
        )
