modelframe
==========

[![Project
Status](http://www.repostatus.org/badges/latest/concept.svg)](http://www.repostatus.org/#concept)
[![travis](https://img.shields.io/travis/dirmeier/modelframe/master.svg?&logo=travis)](https://travis-ci.org/dirmeier/modelframe/)
[![codecov](https://codecov.io/gh/dirmeier/modelframe/branch/master/graph/badge.svg)](https://codecov.io/gh/dirmeier/modelframe)
[![codacy](https://app.codacy.com/project/badge/Grade/c101def3b1d34481a3b72109852f4f8d)](https://www.codacy.com/manual/simon-dirmeier/modelframe?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dirmeier/modelframe&amp;utm_campaign=Badge_Grade)
[![version](https://img.shields.io/pypi/v/modelframe.svg?colorB=black&style=flat)](https://pypi.org/project/modelframe/)

> Compute fixed and random effects model matrices in Python

About
-----

`modelframe` builds model matrices and response vectors from a given
dataset using `lme4`-style formulas in Python. For instance, consider the `sleepstudy` data from
[`lme4`](https://cran.r-project.org/web/packages/lme4/index.html):

``` python
from modelframe import model_frame, load_data

sleepstudy = load_data()
sleepstudy
```

    ##      Reaction  Days Subject
    ## 0    249.5600     0     308
    ## 1    258.7047     1     308
    ## 2    250.8006     2     308
    ## 3    321.4398     3     308
    ## 4    356.8519     4     308
    ## ..        ...   ...     ...
    ## 175  329.6076     5     372
    ## 176  334.4818     6     372
    ## 177  343.2199     7     372
    ## 178  369.1417     8     372
    ## 179  364.1236     9     372
    ## 
    ## [180 rows x 3 columns]

Computing the model matrices is then as simple as:

``` python
frame = model_frame("~ Days + (Days | Subject)", sleepstudy)
```

The fixed effects model matrix:

``` python
frame.coef_model_matrix
```

    ##      Intercept  Days
    ## 0          1.0     0
    ## 1          1.0     1
    ## 2          1.0     2
    ## 3          1.0     3
    ## 4          1.0     4
    ## ..         ...   ...
    ## 175        1.0     5
    ## 176        1.0     6
    ## 177        1.0     7
    ## 178        1.0     8
    ## 179        1.0     9
    ## 
    ## [180 rows x 2 columns]


The random effects model matrix:

``` python
frame.ranef_model_matrix
```

    ##       Intercept Days Intercept Days  ... Intercept Days Intercept Days
    ## group       308  308       309  309  ...       371  371       372  372
    ## 0           1.0  0.0       0.0  0.0  ...       0.0  0.0       0.0  0.0
    ## 1           1.0  1.0       0.0  0.0  ...       0.0  0.0       0.0  0.0
    ## 2           1.0  2.0       0.0  0.0  ...       0.0  0.0       0.0  0.0
    ## 3           1.0  3.0       0.0  0.0  ...       0.0  0.0       0.0  0.0
    ## 4           1.0  4.0       0.0  0.0  ...       0.0  0.0       0.0  0.0
    ## ..          ...  ...       ...  ...  ...       ...  ...       ...  ...
    ## 175         0.0  0.0       0.0  0.0  ...       0.0  0.0       1.0  5.0
    ## 176         0.0  0.0       0.0  0.0  ...       0.0  0.0       1.0  6.0
    ## 177         0.0  0.0       0.0  0.0  ...       0.0  0.0       1.0  7.0
    ## 178         0.0  0.0       0.0  0.0  ...       0.0  0.0       1.0  8.0
    ## 179         0.0  0.0       0.0  0.0  ...       0.0  0.0       1.0  9.0
    ## 
    ## [180 rows x 36 columns]

Installation
------------

You can install `modelframe` either from PyPI using:

```bash
pip install modelframe
```

or using the latest GitHub [release](https://github.com/dirmeier/modelframe/releases/):

```bash
python -m pip install git+https://github.com/dirmeier/modelframe.git
```



Author
------

Simon Dirmeier <a href="mailto:simon.dirmeier @ gmx.de">simon.dirmeier @ gmx.de</a>
