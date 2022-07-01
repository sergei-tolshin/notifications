#! /usr/bin/env bash

set -e

PS4='# '
set -x

./wait-for-it.sh postgres:5432

python3 manage.py migrate

python3 manage.py createsuperuserwithpassword \
        --username admin \
        --password admin \
        --email admin@example.org \
        --preserve

exec "$@"