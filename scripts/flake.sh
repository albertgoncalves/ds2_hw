#!/usr/bin/env bash

cd $WD

for f in src/*.py; do
    echo "linting $f"
    flake8_ignore $f
done
