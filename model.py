import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree



from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


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


def svc_modeling_function(X_train, y_train):    
    weights = {0: 1, 1: 75}
    svclassifier = SVC(kernel='sigmoid', probability = True, gamma = 10, C = 10, class_weight = weights)
    svclassifier.fit(X_train, y_train)

    y_pred = svclassifier.predict(X_train)
    print(confusion_matrix(y_train,y_pred))
    print(classification_report(y_train,y_pred))

    return 


def get_decision_tree(X_train,y_train,X_test,y_test):
    '''
    Prints stats for decision tree model
    '''
    
    # Create decision tree object
    clf = DecisionTreeClassifier(class_weight='balanced', criterion='entropy', max_depth=6,
                                 max_features=None, max_leaf_nodes=None,
                                 min_impurity_decrease=0.0, min_impurity_split=None,
                                 min_samples_leaf=1, min_samples_split=2,
                                 min_weight_fraction_leaf=0.0, presort=False, random_state=123,
                                 splitter='best')
    
    # Fit data to classifier 
    clf = clf.fit(X_train, y_train)

    # Make predictions
    y_pred = clf.predict(X_train)

    # Get probabilities 
    y_pred_proba = clf.predict_proba(X_train)
  
    # Print accuracy
    print('Accuracy of Decision Tree classifier on training set: {:.2f}'
    .format(clf.score(X_train, y_train)))
    
    # Get labels
    labels = sorted(y_train.early_failure.unique())

    print('')
    
    # Print confusion matrix
    print("Confusion Matrix:")
    print(pd.DataFrame(confusion_matrix(y_train, y_pred), index=labels, columns=labels))
    
    print('')
    
    # Print classification report
    print("Classification Report:")
    print(classification_report(y_train, y_pred))