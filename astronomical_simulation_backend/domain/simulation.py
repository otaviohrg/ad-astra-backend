import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Tuple


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
            status="CREATED",
        )

    def update_from_content(self, params: Dict[str, str]) -> None:
        for key in params.keys():
            if key == "k":
                self.k = float(params[key])
            if key == "degree":
                self.degree = float(params[key])

    def get_parameters(self) -> Tuple[float, float]:
        return self.k, self.degree

    def change_state(self, state: str) -> None:
        self.status = state
