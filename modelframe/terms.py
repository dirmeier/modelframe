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


def get_random_effects_terms(rhs):
    ext = _find_within(rhs, r"\(.*?\)")
    terms = []

    for ex in ext:
        terms.append(_ranef_strip(ex.group(0)))

    if not re.match(r".*\(.*\).*", rhs) and "|" in rhs:
        if all(x in rhs for x in ["|", "+"]):
            raise ValueError("your formula isn't built correctly")
        terms.append(_ranef_strip(rhs))

    return terms


def get_fixed_effects_terms(rhs):
    ext = _find_within(rhs, r"\(.*?\)")

    for ex in ext:
        rhs = _coef_strip(rhs, ex)
    els = rhs.split("+")
    if els[0] == "" or (len(els) == 1 and "|" in els[0]):
        els = ["1"]

    terms = []
    for el in els:
        el = el.strip()
        if el != "" and "|" not in el:
            terms.append(el)
        elif el == "":
            raise ValueError("your formula isn't built correctly")
    return terms


def _find_within(text, pattern):
    return re.finditer(pattern, text)


def _search(text, pattern):
    return re.search(pattern, text)


def _coef_strip(coef, ex):
    return coef.replace(ex.group(0), "").rstrip(r" |+").lstrip(" |+")


def _ranef_strip(ranef):
    return ranef.strip().rstrip(")").lstrip("(").replace(" ", "")
