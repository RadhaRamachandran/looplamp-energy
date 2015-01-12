# create csv of data for Loop Lamp's budget mode

import os
import pandas as pd
import MySQLdb as sqd
import pandas.io.sql as sql

# connect to database
mydb = sqd.connect(host = '127.0.0.1', user = 'root', db = 'rdcep_amanda')

def write_csv(house_id, budget, numberOfLights):
    
    # extract data for specified house and date
    df_today = sql.read_frame('select datetime, total_energy from readings_dt where house_id= "'+house_id+'" and datetime between "04/01/14 00:00:00" and "04/01/14 23:45:00"',
                    mydb, parse_dates = ['datetime'], index_col = ['datetime'])
    
    # create column of cumulative energy usage
    df_today = df_today.cumsum()
    
    # create column of number of lights to be lit
    df_today['fraction'] = float(numberOfLights) * (float(budget) - df_today) / float(budget)
    
    # get integer values
    df_today['lights'] = df_today['fraction'].astype(int).values
    
    # write to csv
    df_today['lights'].to_csv('/Users/durango/budget_data_' + budget + '.csv')


write_csv('1334', '30', '24')
    
