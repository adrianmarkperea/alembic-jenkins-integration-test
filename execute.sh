docker run \
  -e DB_USER="postgres" \
  -e DB_PASSWORD="postgres" \
  -e DB_HOST="172.17.0.1" \
  -e DB_PORT="5432" \
  -e DB_NAME="postgres" \
  alembic-runner
