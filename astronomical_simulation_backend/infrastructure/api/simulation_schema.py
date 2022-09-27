from pydantic import BaseModel


class SimulationSchema(BaseModel):
    id: str
    k: float
    degree: float
    status: str
