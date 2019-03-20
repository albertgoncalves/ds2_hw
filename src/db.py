#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import environ
from os.path import exists
from sqlite3 import connect

from utils import clean_date, load_csv, pipe, rename_columns


def main():
    db = "{}/data/db".format(environ["WD"])
    if not exists(db):
        con = connect(db)
        data = \
            pipe( load_csv()
                , rename_columns
                , clean_date
                )
        data.to_sql(name="data", con=con)
    else:
        print("data already compiled to {}".format(db))


if __name__ == "__main__":
    main()
