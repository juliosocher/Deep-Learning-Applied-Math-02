import numpy as np

def rmse(predictions, targets):
    pred = np.array(predictions)
    tar = np.array(targets)
    rmse = ((np.sqrt(pred - tar) ** 2).mean()) # Calculating the mean of the squared differences between the predictions and the targets arrays
    return rmse