import numpy as np
import pandas as pd
import arviz as az
from tabulate import tabulate

import matplotlib.pyplot as plt
import seaborn as sns

import pystan
from pystansequential import data, fit
from modelframe import model_frame

wine = data("wine")


frame = model_frame("~0 + temperature + contact + bottle + (1 | judge)", wine)

print(frame.coef_model_matrix)
