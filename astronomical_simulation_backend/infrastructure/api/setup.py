from fastapi import FastAPI

from astronomical_simulation_backend.container import ApplicationContainer
from astronomical_simulation_backend.infrastructure.api import (
    celestial_body_controller,
    simulation_controller,
)


def setup(app: FastAPI, container: ApplicationContainer) -> None:
    # Add other controllers here
    app.include_router(celestial_body_controller.router)
    app.include_router(simulation_controller.router)

    # Inject dependencies
    container.wire(modules=[celestial_body_controller, simulation_controller])
