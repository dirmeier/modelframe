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


class RandomEffectTerm:
    """
    RandomEffectTerm contains data types for a single random effect.

    Attributes
    ----------
    Z : pandas.DataFrame
        design matrix of random effect with column names
    J : numpy.ndarray
        matrix of indicator columns for the different levels of the random
        effect
    """

    def __init__(self, Z, J):
        self._Z = Z
        self._J = J

    def __str__(self):
        return "<random effects term>"

    def __repr__(self):
        return self.__str__()

    @property
    def Z(self):
        """
        Getter for random effects matrix Z.

        Returns
        -------
        pandas.DataFrame
            random effects design matrix
        """

        return self._Z

    @property
    def n_levels(self):
        """
        Returns the number of levels of the random effect.

        Returns
        -------
        int
            the number of different levels the random effect has
        """
        return int(self._Z.shape[1])

    @property
    def n_terms(self):
        """
        Returns the number of coefficients of the random effect.

        Returns
        -------
        int
            the number of different coefficients the random effect has
        """
        return int(self._Z.shape[1] / self._J.shape[1])
