# data wrangling
import pandas as pd
import numpy as np

# model preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# model and evaluate
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix


def split_my_data(df):
    # define target and features
    X = df.drop(columns = ['model', 'serial_number', 'early_failure', 'failure', 'drive_age_in_years'])
    y = df[['early_failure']]

    # split into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = .80, random_state = 123, stratify=df.early_failure)
    return X_train, X_test, y_train, y_test


def encode_hot(train, test, col_name):
    encoded_values = sorted(list(train[col_name].unique()))

    # Integer Encoding
    int_encoder = LabelEncoder()
    train.encoded = int_encoder.fit_transform(train[col_name])
    test.encoded = int_encoder.transform(test[col_name])

    # create 2D np arrays of the encoded variable (in train and test)
    train_array = np.array(train.encoded).reshape(len(train.encoded),1)
    test_array = np.array(test.encoded).reshape(len(test.encoded),1)

    # One Hot Encoding
    ohe = OneHotEncoder(sparse=False, categories='auto')
    train_ohe = ohe.fit_transform(train_array)
    test_ohe = ohe.transform(test_array)

    # Turn the array of new values into a data frame with columns names being the values
    # and index matching that of train/test
    # then merge the new dataframe with the existing train/test dataframe
    # and drop original column
    train_encoded = pd.DataFrame(data=train_ohe, columns=encoded_values, index=train.index)
    train = train.join(train_encoded)
    train = train.drop(columns = col_name)

    test_encoded = pd.DataFrame(data=test_ohe, columns=encoded_values, index=test.index)
    test = test.join(test_encoded)
    test = test.drop(columns = col_name)

    return train, test


def svc_modeling_function(X_train, y_train, X_test):    
    #create object and fit
    svclassifier = SVC(kernel='rbf', probability = True, C = 100, random_state=123)
    svclassifier.fit(X_train, y_train)

    #predict on train
    y_pred = svclassifier.predict(X_train)
    y_pred_proba = svclassifier.predict_proba(X_train)

    #predict on test
    y_pred_test = svclassifier.predict(X_test)
    
    return y_pred, y_pred_test


def dt_modeling_function(X_train, y_train, X_test):
    #create object and fit 
    clf = DecisionTreeClassifier(class_weight='balanced', criterion='entropy', max_depth=6, max_features=None, max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None, min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0, presort=False, random_state=123, splitter='best')
    clf = clf.fit(X_train, y_train)

    #predict on train
    y_pred = clf.predict(X_train)
    y_pred_proba = clf.predict_proba(X_train)

    #predict on test
    y_pred_test = clf.predict(X_test)
    
    return y_pred, y_pred_test
  
 
def logit_modeling_function(X_train, y_train, X_test):
    #create object and fit
    logit = LogisticRegression(solver = 'liblinear', class_weight='balanced', random_state = 123)
    logit.fit(X_train, y_train)
    
    #predict on train
    y_pred = logit.predict(X_train)
    y_pred_proba = logit.predict_proba(X_train)

    #predict on test
    y_pred_test = logit.predict(X_test)
    
    return y_pred, y_pred_test


def knn_modeling_function(X_train, y_train, X_test):
    #create object and fit
    knn = KNeighborsClassifier(n_neighbors=3, weights = 'distance')
    knn.fit(X_train, y_train)

    #predict on train
    y_pred=knn.predict(X_train)

    #predict on test
    y_pred_test = svclassifier.predict(X_test)
    
    return y_pred, y_pred_test


def evaluate(y, y_pred):
    print(confusion_matrix(y, y_pred))
    print()
    print(classification_report(y, y_pred))