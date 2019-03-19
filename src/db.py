#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import environ
from os.path import exists
from sqlite3 import connect

from pandas import to_datetime

from utils import load_csv, pipe, rename_columns


def prep(data):
    data.summons_date = to_datetime(data.summons_date).astype(str)
    return data.copy()


if __name__ == "__main__":
    directory = environ["WD"]
    db = "{}/db".format(directory)
    if not exists(db):
        con = connect("{}/db".format(directory))
        data = \
            pipe( load_csv()
                , rename_columns
                , prep
                )
        data.to_sql(name="data", con=con)
    else:
        print("data already compiled to {}".format(db))
