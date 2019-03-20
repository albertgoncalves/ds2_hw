#!/usr/bin/env bash

set -e

cd $WD
. .alias

db="data/db"

if [ ! -f $db ]; then
    echo "db not found, rebuilding..."
    python src/db.py
fi

if [[ $1 = "file" ]]; then
    sql="$(cat $2)"
elif [[ $1 = "columns" ]]; then
    sql="PRAGMA table_info(data);"
else
    sql=$1
fi

sqlite3 -csv -header -separator ";" $db "$sql"
