# 100x100 matrix random floating points inside
# each row is a data point
# each column is a feature
# standardize each feature

import numpy as np
import pandas as pd

def standardize_features(array: np.array):
    # for each column, (datapoint - mean) / std
    
    mean_vector = np.mean(array, axis=0)
    std_vector = np.std(array, axis=0)
    standardized_matrix = array - mean_vector / std_vector
    
    return standardized_matrix
