#MAE para ver cuanto es la media de diferencia de error

import sklearn.metrics as metrics
import pandas as pd

def regression_results(y_true, y_pred):
     mean_absolute_error=metrics.mean_absolute_error(y_true, y_pred)
     print('MAE: ', round(mean_absolute_error,4))
     return round(mean_absolute_error,4)


def encode_OneHot(df,column):
    dummies = pd.get_dummies(df[column])
    df = pd.concat([df,dummies], axis=1)
    df = df.drop(column, axis=1)
    return df