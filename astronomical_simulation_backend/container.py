from dependency_injector import containers, providers

from astronomical_simulation_backend.application.celestial_body_service import (
    CelestialBodyService,
)
from astronomical_simulation_backend.application.simulation_service import (
    SimulationService,
)
from astronomical_simulation_backend.infrastructure.database.celestial_body_repository import (
    CelestialBodyPickleRepository,
)
from astronomical_simulation_backend.infrastructure.database.simulation_repository import (
    SimulationPickleRepository,
)


class ApplicationContainer(containers.DeclarativeContainer):
    configuration = providers.Configuration()

    celestial_body_repository = providers.Singleton(
        CelestialBodyPickleRepository,
        storage_dir=configuration.storage_dir + "/celestial_bodies"
    )

    simulation_repository = providers.Singleton(
        SimulationPickleRepository,
        storage_dir=configuration.storage_dir + "/simulation"
    )

    celestial_body_service = providers.Factory(
        CelestialBodyService,
        celestial_body_repository=celestial_body_repository
    )

    simulation_service = providers.Factory(
        SimulationService,
        celestial_body_repository=celestial_body_repository,
        simulation_repository=simulation_repository
    )
