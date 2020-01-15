from sklearn.model_selection import train_test_split
import pandas as import pd
import numpy as np

def split_my_data(df):
    X = df.drop(columns = ['early_failure', 'failure'])
    y = df[['early_failure']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = .80, random_state = 123, stratify=df.early_failure)
    return X_train, X_test, y_train, y_test

