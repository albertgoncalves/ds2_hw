#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
from json import dumps

from utils import load_csv, pipe, rename_columns


def examine(data, column):
    n = len(data)
    n_null = sum(data[column].isnull())
    n_unique = data[column].nunique()
    return \
        { "column": column
        , "n": n
        , "pct_nan": n_null / n
        , "n_unique": n_unique
        , "table": Counter(data[column]) if n_unique < 50 else Counter([])
        }


if __name__ == "__main__":
    data = \
        pipe( load_csv()
            , rename_columns
            )
    def pipeline(column):
        return pipe(column, lambda column: examine(data, column))
    pipe( map(pipeline, data.columns)
        , list
        , dumps
        , print
        )
