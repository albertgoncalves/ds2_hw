#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter

from pandas import read_csv


def clean_date(data):
    data.summons_date = to_datetime(data.summons_date).astype(str)
    return data.copy()


def histogram(xs):
    return sorted(Counter(xs).items(), key=lambda kv: kv[1])


def load_csv():
    csv = "data/nypd_criminal_court_summons_incidents.csv"
    return read_csv(csv)


def pipe(x, *fs):
    for f in fs:
        x = f(x)
    return x


def rename_columns(data):
    columns = \
        { "SUMMONS_KEY": "summons_key"
        , "SUMMONS_DATE": "summons_date"
        , "OFFENSE_DESCRIPTION": "offense_description"
        , "LAW_SECTION_NUMBER": "law_section_number"
        , "LAW_DESCRIPTION": "law_description"
        , "SUMMONS_CATEGORY_TYPE": "summons_category_type"
        , "AGE_GROUP": "age_group"
        , "SEX": "sex"
        , "RACE": "race"
        , "JURISDICTION_CODE": "jurisdiction_code"
        , "BORO": "borough"
        , "PRECINCT_OF_OCCUR": "precinct_of_occurrence"
        , "X_COORDINATE_CD": "x_coordinate_cd"
        , "Y_COORDINATE_CD": "y_coordinate_cd"
        , "Latitude": "lat"
        , "Longitude": "lng"
        }
    return data.rename(columns=columns).copy()


def unzip(xy):
    xs = []
    ys = []
    for (x, y) in xy:
        xs.append(x)
        ys.append(y)
    return xs, ys
