from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, f1_score

def regression_metrics(y_true, y_pred):
    rmse = mean_squared_error(y_true, y_pred, squared=False)
    mae  = mean_absolute_error(y_true, y_pred)
    r2   = r2_score(y_true, y_pred)
    return {"RMSE": rmse, "MAE": mae, "R2": r2}

def classification_metrics(y_true, y_pred):
    f1 = f1_score(y_true, y_pred, pos_label="high")
    return {"F1_high": f1}
