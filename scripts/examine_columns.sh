#!/usr/bin/env bash

set -e

cd $WD

python src/examine_columns.py | jq '.' | less
