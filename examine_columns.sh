#!/usr/bin/env bash

python src/examine_columns.py | jq '.' | less
