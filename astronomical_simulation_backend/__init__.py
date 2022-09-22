import importlib_metadata

try:
    __version__ = importlib_metadata.version(__package__)
except (NameError, importlib_metadata.PackageNotFoundError):
    __version__ = "dev"
