#!/usr/bin/env bash

for f in *.py; do
    echo $f
    flake8_ignore $f
done
