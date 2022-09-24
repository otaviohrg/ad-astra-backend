from dataclasses import asdict
from typing import Dict, List, Optional

from dependency_injector.wiring import Provide
from fastapi import APIRouter

from astronomical_simulation_backend.application.celestial_body_service import (
    CelestialBodyService,
)
from astronomical_simulation_backend.container import ApplicationContainer
from astronomical_simulation_backend.infrastructure.api.celestial_body_schema import (
    CelestialBodySchema,
)

celestial_body_service: CelestialBodyService = Provide[
    ApplicationContainer.celestial_body_service
]

router = APIRouter(
    prefix="/astronomical_simulation",
    tags=["AstronomicalSimulation"],
    responses={404: {"description": "Not found"}},
)


@router.get("/list_celestial_bodies/", response_model=List[CelestialBodySchema])
async def list_celestial_bodies(
    search: Optional[str] = None,
) -> List[CelestialBodySchema]:
    celestial_bodies = celestial_body_service.get_all(search)
    return [
        CelestialBodySchema(**asdict(celestial_body))
        for celestial_body in celestial_bodies
    ]


@router.post("/add_celestial_body/")
async def add_celestial_body(content: Dict[str, str]) -> str:
    return celestial_body_service.add_entry(content)


@router.patch("/remove_celestial_body/")
async def remove_celestial_body(body: Dict[str, str]) -> None:
    return celestial_body_service.remove_entry(body["id"])


@router.patch("/edit_celestial_body/")
async def edit_celestial_body(body: Dict[str, str]) -> None:
    return celestial_body_service.edit_entry(body)
