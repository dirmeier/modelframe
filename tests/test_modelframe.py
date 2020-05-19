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


import unittest

import numpy as np
import pytest

from modelframe import model_frame, load_data


class TestModelFrame(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = load_data()

    def test_load(self):
        data = load_data()
        assert data.shape == (180, 3)
        assert sorted(list(data.columns)) == sorted(["Days", "Reaction", "Subject"])
        assert data.Days.dtype == "int64"
        assert data.Reaction.dtype == "float64"
        assert data.Subject.dtype == "category"

    def test_full_formula(self):
        frame = model_frame("Reaction ~ Days + (Days | Subject)", self.data)
        assert frame.response.shape == (180, )
        assert len(frame.ranef_list) == 1
        assert frame.coef_model_matrix.shape == (180, 2)
        assert frame.ranef_model_matrix.shape == (180, 2 * len(np.unique(self.data["Subject"])))

    def test_single_fixed_variable(self):
        frame = model_frame("~ Days", self.data)
        assert frame.response is None
        assert frame.ranef_list is None
        assert frame.ranef_model_matrix is None
        assert frame.coef_model_matrix.shape == (180, 2)

    def test_single_random_variable(self):
        frame = model_frame("~ 1 | Subject", self.data)
        assert frame.response is None
        assert frame.coef_model_matrix.shape == (180, 1)
        assert frame.ranef_model_matrix.shape == (180, len(np.unique(self.data["Subject"])))

    def test_combination_of_variables(self):
        frame = model_frame("~ Days + (1 | Subject)", self.data)
        assert frame.response is None
        assert frame.coef_model_matrix.shape == (180, 2)
        assert frame.ranef_model_matrix.shape == (180, len(np.unique(self.data["Subject"])))

    def test_another_combination_of_variables(self):
        frame = model_frame("~ Days + (Days | Subject)", self.data)
        assert frame.response is None
        assert frame.coef_model_matrix.shape == (180, 2)
        assert frame.ranef_model_matrix.shape == (180, 2 * len(np.unique(self.data["Subject"])))

    def test_yet_another_combination_of_variables(self):
        frame = model_frame("~ Subject + Days + (Days | Subject)", self.data)
        assert frame.response is None
        assert frame.coef_model_matrix.shape == (180, 2 + len(np.unique(self.data["Subject"])) - 1)
        assert frame.ranef_model_matrix.shape == (180, 2 * len(np.unique(self.data["Subject"])))

    def test_final_combination_of_variables(self):
        frame = model_frame("~ (Days + Reaction | Subject)", self.data)
        assert frame.response is None
        assert frame.coef_model_matrix.shape == (180, 1)
        assert frame.ranef_model_matrix.shape == (180, 3 * len(np.unique(self.data["Subject"])))

    def test_response(self):
        frame = model_frame("Reaction ~ ", self.data)
        assert frame.response.shape == (180,)
        assert frame.coef_model_matrix is None
        assert frame.ranef_model_matrix is None

    def test_bad_formula(self):
        with pytest.raises(ValueError):
            model_frame("~ Days + Reaction | Subject", self.data)

    def test_bad_formula_2(self):
        with pytest.raises(ValueError):
            model_frame("~ Subject | Subject", self.data)

    def test_bad_formula_3(self):
        with pytest.raises(ValueError):
            model_frame("~ Subject ++ Days", self.data)

    def test_bad_response(self):
        with pytest.raises(ValueError):
            model_frame("x ~ ", self.data)
