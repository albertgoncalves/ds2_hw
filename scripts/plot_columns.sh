#!/usr/bin/env bash

set -e

cd $WD

python src/plot_columns.py
open pngs/
