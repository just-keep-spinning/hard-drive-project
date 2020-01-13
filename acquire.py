import pandas as pd 
import numpy as np 

import pyspark
from pyspark.sql.functions import max

import os 

# create local spark enviroment
spark = pyspark.sql.SparkSession.builder.getOrCreate()

def aggegrate_data():
    # pull 2016, 2017, 2019 data
    df_2016 = spark.read.csv('./data/data_Q*_2016/*.csv', header=True)
    df_2017 = spark.read.csv('./data/data_Q*_2017/*.csv', header=True)
    df_2019 = spark.read.csv('./data/data_Q*_2019/*.csv', header=True)

    # pull 2018 data by quarter, as they have different columns
    df_2018_1 = spark.read.csv('./data/data_Q1_2018/*.csv', header=True)
    df_2018_2 = spark.read.csv('./data/data_Q2_2018/*.csv', header=True)
    df_2018_3 = spark.read.csv('./data/data_Q3_2018/*.csv', header=True)
    df_2018_4 = spark.read.csv('./data/data_Q4_2018/*.csv', header=True)

    # find stats that aren't included in older years
    cols_2016 = df_2016.columns
    cols_2019 = df_2019.columns
    remove_traits_list = list(set(cols_2019).difference(cols_2016))

    # remove the established stats
    for trait in remove_traits_list:
        df_2018_1 = df_2018_1.drop(trait)
        df_2018_2 = df_2018_2.drop(trait)
        df_2018_3 = df_2018_3.drop(trait)
        df_2018_4 = df_2018_4.drop(trait)
        df_2019 = df_2019.drop(trait)

    # combine all dfs together
    df = df_2016.union(df_2017).union(df_2018_1).union(df_2018_2).union(df_2018_3).union(df_2018_4).union(df_2019)
    return df

def extract_smart_5(df):
    df = df.groupby('serial_number', 'model', 'capacity_bytes'
                   ).agg(max('failure'), max('smart_9_raw'), max('smart_5_raw'), 
                        max('smart_187_raw') , max('smart_197_raw'), max('smart_198_raw')
                        )
    return df


def acquire_agg_data():
    filename = "hard_drives_smart_5.csv"

    if os.path.exists(filename):
        return pd.read_csv('hard_drives_smart_5.csv').drop('Unnamed: 0',axis=1)
    else:   
        # data aggegrated with top 5 smart stats
        df = extract_smart_5(aggegrate_data())

        # convert to pandas
        df = df.select("*").toPandas()

        # save as csv
        df.to_csv(filename)
        return df
