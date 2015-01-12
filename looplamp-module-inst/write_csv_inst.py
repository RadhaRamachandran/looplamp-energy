import os
import pandas as pd
import MySQLdb as sqd
import pandas.io.sql as sql
import csv

mydb = sqd.connect(host = '127.0.0.1', user = 'root', db = 'rdcep_amanda')

df_today = sql.read_frame('select datetime, total_energy from readings_dt where house_id = "1334" and datetime between "2014-04-01 00:00:00" and "2014-04-01 23:45:00"',
                    mydb, parse_dates = ['datetime'], index_col = ['datetime'])

max = df_today['total_energy'].max(axis=1)

df_today['fraction'] = df_today['total_energy'] / max

def categorize(value):
    if value >= .75:
        return 4
    if (value >= .5) & (value < .75):
        return 3
    if (value >= .25) & (value < (.5)):
        return 2
    else:
        return 1

df_today['level'] = df_today['fraction'].apply(categorize)

df_today.to_csv('inst_data.csv')