import logging
from pathlib import Path

import uvicorn
from fastapi import FastAPI

from astronomical_simulation_backend import __version__
from astronomical_simulation_backend.container import ApplicationContainer
from astronomical_simulation_backend.infrastructure.api.setup import setup


def init() -> FastAPI:
    container = ApplicationContainer()

    # Setup logging
    container.configuration.log_level.from_env(
        "ASTRONOMICAL_SIMULATION_LOG_LEVEL", "INFO"
    )

    str_level = container.configuration.log_level()
    numeric_level = getattr(logging, str_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError("Invalid log level: %s" % str_level)
    logging.basicConfig(level=numeric_level)
    logger = logging.getLogger(__name__)
    logger.info("Logging level is set to %s" % str_level.upper())

    # init Database
    container.configuration.storage_dir.from_env(
        "SIMULATION_STORAGE_DIR", "/tmp/astronomical_simulation"
    )
    Path(container.configuration.storage_dir()).mkdir(parents=True, exist_ok=True)
    Path(container.configuration.storage_dir() + "/celestial_bodies").mkdir(
        parents=True, exist_ok=True
    )
    Path(container.configuration.storage_dir() + "/simulation").mkdir(
        parents=True, exist_ok=True
    )

    # Init API and attach the container
    app = FastAPI()
    app.extra["container"] = container

    # Do setup and dependencies wiring
    setup(app, container)

    # TODO add other initialization here

    return app


def start() -> None:
    """Start application"""
    logger = logging.getLogger(__name__)
    logger.info(f"Astronomical Simulation app version: {__version__}")
    app = init()
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8080,
    )


if __name__ == "__main__":
    start()
