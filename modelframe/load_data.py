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


def load_data():
    """
    Load an example data set: the sleepstudy data from the `lme4` R-package.

    Returns
    -------
    pandas.DataFrame
        returns an example data set

    References
    ----------
    .. [1] D. Bates and M. Mächler and B, Bolker and S. Walker,
       "Fitting Linear Mixed-Effects Models Using lme4",
       Journal of Statistical Software, vol. 67,
       pp. 1-48, 2015.
    """

    import os
    import pandas as pd

    dr, _ = os.path.split(__file__)
    df = pd.read_csv(
        os.path.join(dr, "data", "sleepstudy.csv"),
        dtype={"Reaction": "float64", "Days": "int64", "Subject": "category"},
    )
    return df
