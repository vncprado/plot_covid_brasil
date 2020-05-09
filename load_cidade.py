#!/usr/bin/python3

"""
This script downloads two csv files compresses in gz with information about the covid-19
Retrieve confirmed cases and new cases for a defined city (e.g. Parauapebas, PA, Brazil)
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
    df_confirmados = pd.read_csv(f)
with gzip.open(file_caso_full, 'rb') as f:
    df_novos = pd.read_csv(f)

cidade = "Belém"
estado = "PA"

cidade_confirmados_df = df_confirmados.loc[df_confirmados["place_type"] == "city"]
cidade_confirmados_df = cidade_confirmados_df.loc[cidade_confirmados_df["state"] == estado]
cidade_confirmados_df = cidade_confirmados_df.loc[cidade_confirmados_df["city"] == cidade]

cidade_novos_df = df_novos.loc[df_novos["place_type"] == "city"]
cidade_novos_df = cidade_novos_df.loc[cidade_novos_df["state"] == estado]
cidade_novos_df = cidade_novos_df.loc[cidade_novos_df["city"] == cidade]

datas_confirmados = cidade_confirmados_df['date']
confirmados = cidade_confirmados_df['confirmed']

datas_novos = cidade_novos_df['date']
novos = cidade_novos_df['new_confirmed']

cidade_confirmados = pd.concat([datas_confirmados, confirmados], axis=1).reset_index(drop=True)
cidade_confirmados.to_csv(cidade.lower() + "_" + estado + "_confirmados.csv")

cidade_novos = pd.concat([datas_novos, novos], axis=1).reset_index(drop=True)
cidade_novos.to_csv(cidade.lower() + "_" + estado + "_novos.csv")

to_plot = True
if to_plot:
    x = datas_confirmados
    y = confirmados
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
