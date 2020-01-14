def early_failure(df):
    '''
    add column to identify early failures based on the age of the hard drive 

    '''
    
    df['early_failure']= 1
    df['early_failure'][df.drive_age_in_years<=1.6] = 1
    df['early_failure'][df.drive_age_in_years>1.6] = 0
    
    return df

def get_quartile(df):
    '''
    add colulmn to identify which quartile drive falls in based on the age of the hard drive
    '''
    
    df['quartile']= 1
    df['quartile'][df.drive_age_in_years<1.6] = 'Q1'
    df['quartile'][(df.drive_age_in_years>=1.6) & (df.drive_age_in_years<2.6)] = 'Q2'
    df['quartile'][(df.drive_age_in_years>=2.6) & (df.drive_age_in_years<4)] = 'Q3'
    df['quartile'][(df.drive_age_in_years>=4)] = 'Q4'
    
    return df