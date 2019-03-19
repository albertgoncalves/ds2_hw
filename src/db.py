#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import environ
from os.path import exists
from sqlite3 import connect

from pandas import to_datetime

from utils import clean_date, load_csv, pipe, rename_columns


def main():
    directory = environ["WD"]
    db = "{}/db".format(directory)
    if not exists(db):
        con = connect("{}/db".format(directory))
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
