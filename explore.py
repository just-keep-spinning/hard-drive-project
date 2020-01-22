import pandas as pd 
import numpy as np 

import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

from scipy import stats


def remove_manufacturers(df):
    
    # Remove manufactures with low value counts
    df = df[(df.manufacturer != 'Samsung') & (df.manufacturer != 'Unknown')]
    return df


def early_failure(df,cut_off=2.6):
    '''
    Add column to identify early failures based on the age of the hard drive 

    '''
    df['early_failure'] = np.where((df.drive_age_in_years <= cut_off) & (df.failure == 1), 1, 0)
    
    return df

def old_or_fail(df,cut_off=2.6):
    '''
    Retain rows for drives that have failed or are older than the cut off age
    '''

    df = df[(df.failure==1)|(df.drive_age_in_years > cut_off)]

    return df

def make_binary_values(df):
    df.reallocated_sectors_count = np.where(df.reallocated_sectors_count > 0, '1','0').astype(bool)
    df.reported_uncorrectable_errors = np.where(df.reported_uncorrectable_errors > 0, '1', '0').astype(bool)
    df.command_timeout = np.where(df.command_timeout > 0, '1', '0').astype(bool)
    df.current_pending_sector_count = np.where(df.current_pending_sector_count > 0, '1', '0').astype(bool)
    df.uncorrectable_sector_count = np.where(df.uncorrectable_sector_count > 0, '1', '0').astype(bool)
    return df


def get_quartile(df,Q1=1.6,Q2=2.6,Q3=4):
    '''
    Add colulmn to identify which quartile drive falls in based on the age of the hard drive
    '''
    
    df['quartile']= 1
    df['quartile'][df.drive_age_in_years<Q1] = 'Q1'
    df['quartile'][(df.drive_age_in_years>=Q1) & (df.drive_age_in_years<Q2)] = 'Q2'
    df['quartile'][(df.drive_age_in_years>=Q2) & (df.drive_age_in_years<Q3)] = 'Q3'
    df['quartile'][(df.drive_age_in_years>=Q3)] = 'Q4'
    
    return df

def chi2_models(df):
    stats_list = [] # empty list for stats

    for mode in df.model.unique():
        # create a for each model vs all other models
        observed = pd.crosstab(df.model == mode, df.early_failure)

        # run chi2 test
        chi2, p, degf, expected = stats.chi2_contingency(observed)

        # format variables and define significance 
        chi2 = round(chi2,4)
        p = round(p,4)
        signif = p < 0.05

        # append every model's values to list
        stats_list.append([mode, chi2, p, signif])

    return pd.DataFrame(stats_list, columns=['model','chi2', 'p', 'signif'])
    

def get_manufacturer_graph(df):

    df = df[['model','manufacturer','drive_age_in_years']]

    df = df.groupby('model').agg({'manufacturer': 'max','drive_age_in_years':'median'})

    df = get_quartile(df)

    df = df.drop(columns=['drive_age_in_years'])
    df = df.reset_index()

    df['count']= 1

    df = df.groupby(['manufacturer','quartile']).count().reset_index()

    sns.barplot(x='manufacturer', y='count', hue='quartile', data=df, palette='Blues')
    plt.title("Model Reliability by Manufacturer ")