# modelframe: Compute fixed and random effects model matrices in Python
#
# Copyright (C) Simon Dirmeier
#
# This file is part of modelframe.
#
# modelframe is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# modelframe is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with modelframe. If not, see <http://www.gnu.org/licenses/>.
#
#
# @author = 'Simon Dirmeier'
# @email = 'simon.dirmeier@web.de'


import re

import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.preprocessing import LabelEncoder

from modelframe import khatri_rao
from modelframe.terms import get_random_effects_terms, get_fixed_effects_terms


def build_intercept_matrix(len) -> pd.Series:
    return pd.Series(np.ones(shape=(len)), name="Intercept")


def random_effects_model_matrix(covars, factor, data):
    J = pd.get_dummies(pd.Series(data[factor])).values

    if len(covars) == 1 and covars[0] == "1":
        X = build_intercept_matrix(J.shape[0]).values.reshape((J.shape[0], 1))
    else:
        X = fixed_effects_model_matrix(covars, data, True).values

    Z = pd.DataFrame(
        khatri_rao(J.T, X.T).T,
    )

    print(Z)

    X = fixed_effects_model_matrix(covars, data, True)
    X['grp'] = data[factor]
    X = X[["Intercept"] + covars + ["grp"]].pivot(columns="grp").reindex()
    X.values[np.isnan(X.values)] = 0
    X = X.reindex(sorted(X.columns, key=lambda x: x[1]), axis=1)
    print(X)
    X = fixed_effects_model_matrix(["0"] + covars, data, True)

    # print(X)


    return Z, Z.shape[1] / J.shape[1]


def random_effects_model_matrices(terms, data):
    ranef_regex = re.compile("(.+) *\\| *(.+)")
    Zlist = []
    n_terms_list = []
    for el in terms:
        reg = ranef_regex.match(el)
        covars, factor = reg.group(1), reg.group(2)
        covars = get_fixed_effects_terms(covars)
        Zi, n_terms = random_effects_model_matrix(covars, factor, data)
        Zlist.append(Zi)
        n_terms_list.append(n_terms)


def build_series(rhs, data, error_no_categorical):
    el = rhs.strip().replace("(", "").replace(")", "")
    series = data[el]
    if series.dtype == "int64" or series.dtype == "float64":
        return series
    elif series.dtype == "bool":
        return pd.Series(data[el].values, dtype="int64")
    elif series.dtype == "category" or series.dtype == "category":
        if error_no_categorical:
            raise ValueError("no categorical variables implemented yet")
        return pd.get_dummies(series, drop_first=True)
    else:
        raise ValueError(f"dtype '{series.dtype}' of column '{el}' is not supported")


def fixed_effects_model_matrix(terms, data, error_no_categorical=False):
    X = []
    for el in terms:
        if el != "0":
            X += [build_series(el, data, error_no_categorical)]
    if "0" not in terms:
        X.insert(0, build_intercept_matrix(data.shape[0]))

    return pd.concat(X, axis=1)


def compute_model_matrices(rhs, data):
    coef_terms = get_fixed_effects_terms(rhs)
    ranef_terms = get_random_effects_terms(rhs)

    X = fixed_effects_model_matrix(coef_terms, data)
    Z = random_effects_model_matrices(ranef_terms, data)
    # print(Z)

    # return {
    #     "X": X,
    #     "Z": Z
    # }


def model_frame(formula: str, data: DataFrame):
    if "~" not in formula:
        raise ValueError("formula needs to contain a '~'")
    els = list(map(lambda x: x.strip(), formula.split("~")))
    compute_model_matrices(els[1], data)


