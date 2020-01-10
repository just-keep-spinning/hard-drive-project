import pandas as pd
import numpy as np
import re 


def prepare(df):
    
    # Drop normalized columns
    columns = []
    for i in df.columns:
        columns.append(i)
    columns = str(columns)
    normalized_columns = re.findall(r'(smart_\d+_normalized)', columns)
    df.drop(columns=normalized_columns, inplace=True)
    
    # Convert capacity column from bytes to gigabytes
    df['capacity_bytes'] = round((df['capacity_bytes']/ 1_000_000_000),1)

    
    # Convert power hours to days
    df['smart_9_raw'] = round((df['smart_9_raw']/ 24),1)

    # Rename columns appropriately
    df.rename(columns={'capacity_bytes':'capacity_gigabytes','smart_9_raw':'drive_age_in_days'}, inplace = True)
    
    return df