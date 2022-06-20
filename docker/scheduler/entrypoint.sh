#! /usr/bin/env bash

set -e

PS4='# '
set -x

./wait-for-it.sh admin:8000

exec "$@"