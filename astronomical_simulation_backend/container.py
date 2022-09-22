from dependency_injector import containers, providers

from astronomical_simulation_backend.application.celestial_body_service import (
    CelestialBodyService,
)
from astronomical_simulation_backend.infrastructure.database.celestial_body_repository import (
    CelestialBodyPickleRepository,
)


class ApplicationContainer(containers.DeclarativeContainer):
    configuration = providers.Configuration()

    celestial_body_repository = providers.Singleton(
        CelestialBodyPickleRepository, storage_dir=configuration.storage_dir
    )

    celestial_body_service = providers.Factory(
        CelestialBodyService, celestial_body_repository
    )
