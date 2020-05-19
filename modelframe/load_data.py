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
    Load an example data set: the sleepstudy data from the `lme4` R-package, published in:

    @article{,
       author = {Douglas Bates and Martin Mächler and Ben Bolker and Steve Walker},
       title = {Fitting Linear Mixed-Effects Models Using lme4},
       journal = {Journal of Statistical Software},
       volume = {67},
       number = {1},
       year = {2015},
       issn = {1548-7660},
       pages = {1--48},
       doi = {10.18637/jss.v067.i01},
       url = {https://www.jstatsoft.org/v067/i01}
    }

    Returns
    -------
    df: pandas.DataFrame
        returns an example data set
    """
    import os
    import pandas as pd

    dir, _ = os.path.split(__file__)
    df = pd.read_csv(
        os.path.join(dir, "data", "sleepstudy.csv"),
        dtype={"Reaction": "float64", "Days": "int64", "Subject": "category"},
    )
    return df
