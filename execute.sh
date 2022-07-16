docker run \
  -it \
  --network="host" \
  -e DB_USER="postgres" \
  -e DB_PASSWORD="postgres" \
  -e DB_HOST="localhost" \
  -e DB_PORT="5432" \
  -e DB_NAME="postgres" \
  alembic-runner
