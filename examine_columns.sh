#!/usr/bin/env bash

python examine_columns.py | jq '.' | less
