# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import json
import logging
import os
import pickle
import numpy as np
import pandas as pd
import joblib

import azureml.automl.core
import azureml.train.automl
from azureml.automl.core.shared import logging_utilities, log_server
from azureml.telemetry import INSTRUMENTATION_KEY

from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType
from inference_schema.parameter_types.pandas_parameter_type import PandasParameterType



input_sample = pd.DataFrame({"age": pd.Series([43], dtype="int64"), "job": pd.Series(["blue-collar"], dtype="object"), "marital": pd.Series(["single"], dtype="object"), "education": pd.Series(["basic.9y"], dtype="object"), "default": pd.Series(["no"], dtype="object"), "housing": pd.Series(["yes"], dtype="object"), "loan": pd.Series(["no"], dtype="object"), "contact": pd.Series(["cellular"], dtype="object"), "month": pd.Series(["jul"], dtype="object"), "duration": pd.Series([982], dtype="int64"), "campaign": pd.Series([1], dtype="int64"), "pdays": pd.Series([999], dtype="int64"), "previous": pd.Series([0], dtype="int64"), "poutcome": pd.Series(["nonexistent"], dtype="object"), "emp.var.rate": pd.Series([1.4], dtype="float64"), "cons.price.idx": pd.Series([93.9179999999999], dtype="float64"), "cons.conf.idx": pd.Series([-42.7], dtype="float64"), "euribor3m": pd.Series([4.963], dtype="float64"), "nr.employed": pd.Series([5228.1], dtype="float64")})
output_sample = np.array([0])

model_path = os.path.join("C:\\Users\\arlio\\OneDrive\\Desktop\\Cognitive\\Containers\\ML", 'model.pkl')
path = os.path.normpath(model_path)
path_split = path.split(os.sep)
model = joblib.load(model_path)
