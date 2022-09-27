from dataclasses import asdict
from typing import Dict, List, Optional

from dependency_injector.wiring import Provide
from fastapi import APIRouter

from astronomical_simulation_backend.application.simulation_service import (
    SimulationService,
)
from astronomical_simulation_backend.container import ApplicationContainer
from astronomical_simulation_backend.infrastructure.api.simulation_schema import (
    SimulationSchema,
)
from astronomical_simulation_backend.infrastructure.api.celestial_body_schema import (
    CelestialBodySchema,
)

simulation_service: SimulationService = Provide[
    ApplicationContainer.simulation_service
]

router = APIRouter(
    prefix="/astronomical_simulation/simulation",
    tags=["AstronomicalSimulation", "Simulation"],
    responses={404: {"description": "Not found"}},
)


@router.get("/list_simulations/", response_model=List[SimulationSchema])
async def list_simulations() -> List[SimulationSchema]:
    simulations = simulation_service.get_all()
    return [
        SimulationSchema(**asdict(simulation))
        for simulation in simulations
    ]


@router.get("/list_simulation_bodies/", response_model=List[CelestialBodySchema])
async def list_celestial_bodies(
    simulation_id: str
) -> List[CelestialBodySchema]:
    celestial_bodies = simulation_service.get_all_bodies(simulation_id)
    return [
        CelestialBodySchema(**asdict(body))
        for body in celestial_bodies
    ]


@router.post("/create_simulation/")
async def create_simulation(params: Dict[str, str]) -> str:
    return simulation_service.add_simulation(params)


@router.patch("/delete_simulation/")
async def delete_simulation(params: Dict[str, str]) -> None:
    return simulation_service.remove_entry(params["id"])


@router.patch("/edit_celestial_body/")
async def edit_simulation(params: Dict[str, str]) -> None:
    return simulation_service.edit_entry(params)
