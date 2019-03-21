#!/usr/bin/env python3

from os import environ

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

from utils import load_csv


def colorbar(ax, mat):
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.5)
    plt.colorbar(mat, cax=cax)


def plot(data, directory):
    corr = data.corr()
    columns = corr.columns
    ticks = range(len(columns))
    fig, ax = plt.subplots(figsize=(10, 10))
    mat = ax.matshow(corr, vmin=-1, vmax=1)
    plt.xticks(ticks, columns, rotation=45, ha="left")
    plt.yticks(ticks, columns)
    colorbar(ax, mat)
    plt.tight_layout()
    plt.savefig("{}/pngs/matrix.png".format(directory))
    plt.close()


def main():
    plot(load_csv(), environ["WD"])


if __name__ == "__main__":
    main()
