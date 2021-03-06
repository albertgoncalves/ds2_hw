#!/usr/bin/env python3

from collections import Counter
from json import dumps

from utils import histogram, load_csv, pipe, rename_columns


def examine(data, column):
    n = len(data)
    n_null = sum(data[column].isnull())
    n_unique = data[column].nunique()
    return \
        { "column": column
        , "n": n
        , "pct_nan": n_null / n
        , "n_unique": n_unique
        , "table":
            pipe( Counter(data[column]) if n_unique < 50 else Counter([])
                , histogram
                , lambda xs: xs[::-1]
                , dict
                )
        }


def pipeline(data):
    def f(column):
        return pipe(column, lambda column: examine(data, column))
    return f


if __name__ == "__main__":
    data = \
        pipe( load_csv()
            , rename_columns
            )
    pipe( map(pipeline(data), data.columns)
        , list
        , dumps
        , print
        )
