#!/usr/bin/python3

"""
This script downloads two csv files compresses in gz with information about the covid-19
Retrieve confirmed cases and new cases for Parauapebas, PA, Brazil
Save this in two separated csv files
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook

import wget
url_caso = "https://data.brasil.io/dataset/covid19/caso.csv.gz"
url_caso_full = "https://data.brasil.io/dataset/covid19/caso_full.csv.gz"
file_caso = './caso.csv.gz'
file_caso_full = './caso_full.csv.gz'

import os
# As file at filePath is deleted now, so we should check if file exists or not not before deleting them
if os.path.exists(file_caso):
    os.remove(file_caso)
if os.path.exists(file_caso_full):
    os.remove(file_caso_full)

wget.download(url_caso, file_caso)
wget.download(url_caso_full, file_caso_full)

import gzip
with gzip.open(file_caso, 'rb') as f:
    df = pd.read_csv(f)
with gzip.open(file_caso_full, 'rb') as f:
    df_full = pd.read_csv(f)

cidade = "Imperatriz"

pebas_df = df.loc[df["place_type"] == "city"]
pebas_df = df.loc[df["city"] == cidade]

pebas_df_full = df_full.loc[df_full["place_type"] == "city"]
pebas_df_full = df_full.loc[df_full["city"] == cidade]

dates = pebas_df['date']
confirmed = pebas_df['confirmed']

dates_full = pebas_df_full['date']
confirmed_full = pebas_df_full['new_confirmed']

pebas = pd.concat([dates, confirmed], axis=1).reset_index(drop=True)
pebas.to_csv(cidade.lower() +"_confirmados.csv")

pebas_full = pd.concat([dates_full, confirmed_full], axis=1).reset_index(drop=True)
pebas_full.to_csv(cidade.lower() + "_novos.csv")

to_plot = False
if to_plot:
    x = dates
    y = confirmed
    years = mdates.YearLocator()   # every year
    months = mdates.MonthLocator()  # every month
    years_fmt = mdates.DateFormatter('%Y')

    fig, ax = plt.subplots()
    ax.plot(x, y)#, 'date', 'adj_close')

    # format the ticks
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(years_fmt)
    ax.xaxis.set_minor_locator(months)

    # round to nearest years.
    # print(x[:0])
    x.iloc[0]
    datemax = np.datetime64(x.iloc[0])
    datemin = np.datetime64(x.iloc[-1])# + np.timedelta64(1)
    ax.set_xlim(datemin, datemax)

    # format the coords message box
    ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
    # ax.format_ydata = lambda x: '$%1.2f' % x  # format the price.
    ax.grid(True)

    # rotates and right aligns the x labels, and moves the bottom of the
    # axes up to make room for them
    fig.autofmt_xdate()

    plt.show()
