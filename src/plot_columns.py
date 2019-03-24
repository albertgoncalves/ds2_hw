#!/usr/bin/env python3

import fiona
from geopandas import GeoDataFrame, read_file
import matplotlib.pyplot as plt
from pandas import to_datetime
from shapely.geometry import Point

from utils import histogram, load_csv, pipe, rename_columns, unzip


def df_to_gdf(data):
    geometry = [Point(xy) for xy in zip(data.lng, data.lat)]
    crs = {"init": "epsg:4326"}
    return GeoDataFrame( data.drop(["lat", "lng"], axis=1).copy()
                       , crs=crs
                       , geometry=geometry
                       )


def string_to_date(column):
    def f(data):
        data[column] = to_datetime(data[column])
        return data.copy()
    return f


def frequency(data, column, n):
    counts = histogram(data[column].values)
    if len(counts) < n:
        n = len(counts)
    labels, x = unzip(counts)
    _, ax = plt.subplots(figsize=(10, 4))
    y = list(range(n))
    ax.barh(y, x[-n:])
    plt.yticks(y, tuple(labels[-n:]), fontsize=7)
    plt.tight_layout()
    plt.savefig("pngs/{}_frequency.png".format(column))
    plt.close()
    return counts, n


def geoplot(data, geodata, column, counts, i, j):
    n = len(counts)
    while (int((i - 1) * j) >= n) & (i > 2):
        i -= 1
    fig, axs = plt.subplots(i, j, figsize=(j * 5, i * 4))
    for k in range(int(i * j)):
        x = k // j
        y = k % j
        if k < n:
            key, value = counts[k]
            alpha = (1 / value) ** 0.4
            subdata = data.loc[data[column] == key].copy()
            geodata.plot(ax=axs[x, y], color="w", edgecolor="k")
            subdata.plot(ax=axs[x, y], alpha=alpha, markersize=5)
            axs[x, y].set_aspect("equal")
            axs[x, y].set_title("\n".join([key, str(value)]), fontsize=9)
        else:
            axs[x, y].set_axis_off()

    plt.tight_layout()
    plt.savefig("pngs/{}_geoplot.png".format(column))
    plt.close()


if __name__ == "__main__":
    geojson = "data/borough_boundaries.geojson"
    geodata = read_file(geojson)
    data = \
        pipe( load_csv()
            , rename_columns
            , string_to_date("summons_date")
            , df_to_gdf
            )
    columns = \
        [ "summons_date"
        , "offense_description"
        , "law_section_number"
        , "law_description"
        , "summons_category_type"
        , "age_group"
        , "sex"
        , "race"
        , "jurisdiction_code"
        , "borough"
        , "precinct_of_occurrence"
        ]
    i = 4
    j = 4
    for column in columns:
        data[column] = data[column].astype(str).fillna("nan")
        counts, n = frequency(data, column, int(i * j))
        geoplot(data, geodata, column, counts[-n:][::-1], i, j)
