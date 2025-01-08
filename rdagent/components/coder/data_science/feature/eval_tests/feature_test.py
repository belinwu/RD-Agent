"""
A qualified data loader should support following features
- successfully run
- len(test) == len(test_ids) == submission length
- len(train) == len(y)

Please make sure the stdout is rich enough to support informative feedback
"""

import pickle

import numpy as np
import pandas as pd
from feature import feat_eng
from load_data import load_data

X, y, X_test, test_ids = load_data()
X, y, X_test = feat_eng(X, y, X_test)


# Validate the conditions mentioned in the docstring
assert X_test.shape[0] == test_ids.shape[0], "Mismatch in length of test images and test IDs"
assert X.shape[0] == y.shape[0], "Mismatch in length of training images and labels"

print("Feature Engineering test passed successfully. Length of test images matches length of test IDs.")
