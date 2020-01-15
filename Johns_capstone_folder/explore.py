def apply_cutoff(df,cut_off=2):
    '''
    Apply cutoff date to the dataframe 
    '''

    # remove the drives that did not fail and that are below the cut off age from the data frame
    df = df[(df.failure==1)|(df.drive_age_in_years > cut_off)]
    # mark remaining units as early failure (1) or not early failure (2)
    df['early_failure']= 1
    df['early_failure'][df.drive_age_in_years>=cut_off] = 1
    df['early_failure'][df.drive_age_in_years>cut_off] = 0
    
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