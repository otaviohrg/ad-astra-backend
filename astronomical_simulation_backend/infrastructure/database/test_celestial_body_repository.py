from tempfile import TemporaryDirectory

import pytest as pytest

from astronomical_simulation_backend.container import ApplicationContainer
from astronomical_simulation_backend.domain.celestial_body import CelestialBody
from astronomical_simulation_backend.infrastructure.database.celestial_body_repository import (
    CelestialBodyPickleRepository,
)


@pytest.fixture()
def repository():
    with TemporaryDirectory() as tmp_dir:
        container = ApplicationContainer()

        container.configuration.storage_dir.from_value(tmp_dir)
        yield container.celestial_body_repository()


def test_add_and_get(repository: CelestialBodyPickleRepository):
    test_input = {
        "name": "TestPlanet",
        "mass": "1234",
        "angular_speed": "12.5",
        "x_coordinate": "200",
        "y_coordinate": "300",
        "x_speed": "20",
        "y_speed": "-30",
        "radius": "150.00",
    }
    entry = CelestialBody.create_from_content(test_input)
    repository.add(entry)
    assert entry == repository.get(entry.id)
