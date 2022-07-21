#!/usr/bin/env bash

read_whitelisted_namespaces_arr() {
  source whitelisted_namespaces.sh
}

read_all_namespaces_arr() {
  source all_namespaces.sh
}

run_alembic() {
  echo "Running alembic"
  for namespace in "${namespaces[@]}"
  do
    python3 -m alembic -name $namespace upgrade head
  done
}

case $ENVIRONMENT_NAME in
  # We only want to run migrations on whitelisted namespaces for prod and pre-prod environments
  prod)
    read_whitelisted_namespaces_arr
    ;;
  preprod)
    read_whitelist_namespaces_arr
    ;;
  *)
    read_all_namespaces_arr
    ;;
esac

run_alembic 
