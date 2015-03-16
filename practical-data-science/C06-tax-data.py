# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 13:36:07 2015

@author: mwakeman
"""

# What does this do?
# add the right libraries

# time to start using matplotlib
import csv
import numpy as np
import matplotlib.pyplot as plt
def dataset(path, filter_field=None,
            filter_value=None):
    with open(path, 'rU') as csvfile:
        reader = csv.DictReader(csvfile)
        if filter_field:
            for row in filter(lambda row: row[filter_field]==filter_value, reader):
                yield row
#                else:
#                    for row in reader:
#                        yield row

                        
    def main(path):
        data = [(row["Year"], float(row["Average income per tax unit"]))
    for row in dataset(path, "Country", "United States")]

    width = 0.35
    ind   = np.arange(len(data))
    fig   = plt.figure()
    ax    = plt.subplot(111)

    ax.bar(ind, list(d[1] for d in data))
    ax.set_xticks(np.arange(0, len(data), 4))
    ax.set_xticklabels(list(d[0] for d in data) [0::4], rotation=45)
    ax.set_ylabel("Income in USD")
    plt.title("U.S. Average Income 1913 - 2012")

    plt.show()
    if __name__ == "__main__":
        main("us_income_trended.csv")