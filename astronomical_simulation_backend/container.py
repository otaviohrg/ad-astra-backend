from dependency_injector import providers, containers

from astronomical_simulation_backend.application.celestial_body_service import CelestialBodyService
from astronomical_simulation_backend.infrastructure.database.celestial_body_repository import CelestialBodyPickleRepository


class ApplicationContainer(containers.DeclarativeContainer):
    configuration = providers.Configuration()

    todo_entry_repository = providers.Singleton(
        CelestialBodyPickleRepository,
        storage_dir=configuration.storage_dir
    )

    todo_service = providers.Factory(
        CelestialBodyService,
        todo_entry_repository
    )