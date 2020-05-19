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

from modelframe.ranef_term import RandomEffectTerm
from modelframe.terms import get_random_effects_terms, get_fixed_effects_terms


class ModelFrame:
    """
    ModelFrame class that contains relevant model matrices and response vector.
    """

    def __init__(self, y, X, Z, Zlist):
        self._y = y
        self._X = X
        self._Z = Z
        self._Zlist = Zlist

    def __str__(self):
        return "<a model frame>"

    def __repr__(self):
        return self.__str__()

    @property
    def response(self):
        """
        Gets the response vector of the model frame

        :return: a pandas Series
        :rtype: pandas.Series
        """
        return self._y

    @property
    def coef_model_matrix(self):
        """
        Gets the model matrix for the fixed, or population-level, coefficients

        :return: a pandas Series
        :rtype: pandas.DataFrame
        """
        return self._X

    @property
    def ranef_model_matrix(self):
        """
        Gets the model matrix for the random, or group-specific, coefficients

        :return: a pandas data frame
        :rtype: pandas.DataFrame
        """
        return self._Z

    @property
    def ranef_list(self):
        """
        Gets the list of separate matrices of random effect terms

        :return: a list of terms
        :rtype: list(RandomEffectTerm)
        """
        return self._Zlist


def model_frame(formula: str, data: DataFrame) -> ModelFrame:
    """

    Parameters
    ----------
    formula: str
        an `lme4`-style formula object. More specifically, a
        (two-sided) linear formula object separated by a ~
    data: pandas.DataFrame
        a data frame containing the variables named in formula

    Returns
    -------
    ModelFrame: a ModelFrame object containing model matrices and response matrix

    Examples
    -------
    >>> from modelframe import load_data
    >>> data = load_data()
    >>> frame = model_frame("Reaction ~ Days + (1 | Subject)", data)
    """

    if "~" not in formula:
        raise ValueError("formula needs to contain a '~'")
    els = list(map(lambda x: x.strip(), formula.split("~")))
    X, Z, Zlist = _compute_model_matrices(els[1], data)
    Y = _compute_response(els[0], data)

    return ModelFrame(Y, X, Z, Zlist)


def _random_effects_model_matrices(terms, data):
    ranef_regex = re.compile("(.+) *\\| *(.+)")
    Zlist = []
    Z = []
    for el in terms:
        reg = ranef_regex.match(el)
        covars, factor = reg.group(1), reg.group(2)
        covars = get_fixed_effects_terms(covars)
        ranef = _random_effects_model_matrix(covars, factor, data)
        Zlist.append(ranef)
        Z.append(ranef.Z)
    if len(Z):
        Z = pd.concat(Z, axis=1)
        return Z, Zlist
    return None, None


def _random_effects_model_matrix(covars, factor, data):
    J = pd.get_dummies(pd.Series(data[factor])).values

    Z, covars = _fixed_effects_model_matrix(covars, data, True)
    Z["group"] = data[factor]

    Z = Z[covars + ["group"]].pivot(columns="group").reindex()
    Z.values[np.isnan(Z.values)] = 0
    Z = Z.reindex(sorted(Z.columns, key=lambda x: x[1]), axis=1)

    return RandomEffectTerm(Z, J)


def _fixed_effects_model_matrix(terms, data, error_no_categorical=False):
    X = []
    for el in terms:
        if el != "0" and el != "1":
            X += [_build_series(el, data, error_no_categorical)]
    if "0" not in terms:
        X.insert(0, _build_intercept_matrix(data.shape[0]))

    if len(X):
        X = pd.concat(X, axis=1)
        return X, list(X.columns)
    return None, None


def _build_intercept_matrix(leng) -> pd.Series:
    return pd.Series(np.ones(shape=leng), name="Intercept")


def _build_series(rhs, data, error_no_categorical):
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


def _compute_model_matrices(rhs, data):
    if rhs.strip() == "":
        return None, None, None

    coef_terms = get_fixed_effects_terms(rhs)
    ranef_terms = get_random_effects_terms(rhs)

    X, _ = _fixed_effects_model_matrix(coef_terms, data)
    Z, Zlist = _random_effects_model_matrices(ranef_terms, data)

    return X, Z, Zlist


def _compute_response(lhs, data):
    lhs = lhs.strip()
    if lhs == "":
        return None
    if lhs in data.columns:
        return data[lhs]
    raise ValueError(f"column '{lhs}' does not exist in data")
