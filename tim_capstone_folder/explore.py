import pandas as pd 
import numpy as np 


def remove_manufacturers(df):
    
    # Remove manufactures with low value counts
    df = df[(df.manufacturer != 'Samsung') & (df.manufacturer != 'Unknown')]
    return df


def early_failure(df,cut_off=1.6):
    '''
    Add column to identify early failures based on the age of the hard drive 
    '''
    df['early_failure'] = np.where((df.drive_age_in_years <= cut_off) & (df.failure == 1), 1, 0)
    
    return df

def old_or_fail(df,cut_off=1.6):
    '''
    Retain rows for drives that have failed or are older than the cut off age
    '''

    df = df[(df.failure==1)|(df.drive_age_in_years > cut_off)]

    return df

def make_binary_values(df):
    df['smart_5_nonzero'] = np.where(df.reallocated_sectors_count > 0, '1','0').astype(int)
    df['smart_187_nonzero'] = np.where(df.reported_uncorrectable_errors > 0, '1', '0').astype(int)
    df['smart_188_nonzero'] = np.where(df.command_timeout > 0, '1', '0').astype(int)
    df['smart_197_nonzero'] = np.where(df.current_pending_sector_count > 0, '1', '0').astype(int)
    df['smart_198_nonzero'] = np.where(df.uncorrectable_sector_count > 0, '1', '0').astype(int)
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