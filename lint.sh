echo "-- Checking import sorting"
isort .

echo "-- Checking python formating"
black .

echo "-- Checking type annotations"
mypy ./astronomical_simulation_backend  --ignore-missing-imports

echo "-- Checking for dead code"
vulture ./astronomical_simulation_backend

echo "-- Checking security issues"
bandit -r ./astronomical_simulation_backend