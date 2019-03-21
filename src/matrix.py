#!/usr/bin/env python3

from os import environ

import matplotlib.pyplot as plt

from utils import load_csv


def plot(data, directory):
    corr = data.corr()
    columns = corr.columns
    fig, ax = plt.subplots(figsize=(10, 10))
    cax = ax.matshow(corr)
    fig.colorbar(cax)
    plt.xticks(range(len(columns)), columns, rotation=45, ha="left")
    plt.yticks(range(len(columns)), columns)
    plt.tight_layout()
    plt.savefig("{}/pngs/matrix.png".format(directory))
    plt.close()


def main():
    plot(load_csv(), environ["WD"])


if __name__ == "__main__":
    main()
