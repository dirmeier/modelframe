modelframe
==========

.. image:: http://www.repostatus.org/badges/latest/wip.svg
   :target: http://www.repostatus.org/#wip
   :alt: Status
.. image:: https://img.shields.io/travis/cbg-ethz/pybda/master.svg?&logo=travis
   :target: https://travis-ci.org/cbg-ethz/pybda/
   :alt: Travis
.. image:: https://codecov.io/gh/cbg-ethz/pybda/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/cbg-ethz/pybda
   :alt: Codecov
.. image:: https://api.codacy.com/project/badge/Grade/a4cca665933a4def9c2cfc88d7bbbeae
   :target: https://www.codacy.com/app/simon-dirmeier/pybda?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=cbg-ethz/pybda&amp;utm_campaign=Badge_Grade
   :alt: Codacy
.. image:: https://readthedocs.org/projects/pybda/badge/?version=latest
   :target: https://pybda.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation
.. image:: https://img.shields.io/pypi/v/pybda.svg?colorB=black&style=flat
   :target: https://pypi.org/project/pybda/
   :alt: PyPi

Compute fixed and random effects model matrices in Python

.. toctree::
   :hidden:
   :maxdepth: 1
   :titlesonly:

   Home <self>
   usage
   examples
   faq
   contributing

About
-----


``modelframe`` builds model matrices and response vectors from a given dataset and an ``lme4``-style formula.
As an example we consider a sleep study data set which is included in ``modelframe``.

.. jupyter-execute::

    from modelframe import model_frame, load_data

    sleepstudy = load_data()
    sleepstudy

The matrices can be computed from the data set like this:

.. jupyter-execute::

    frame = model_frame("Reaction ~ Days + (1 | Subject)", sleepstudy)
    frame


The model above builds a response vector for the variable ``Reaction``, a
fixed model matrix for the variable ``Days`` including an intercept, and a random effects model
matrix with an intercept for every ``Subject``.

The response variable is a ``pandas.Series`` and can then be accessed via:

.. jupyter-execute::

    frame.response


References
----------

 `Douglas Bates and Martin Mächler and Ben Bolker and Steve Walker. "Fitting Linear Mixed-Effects Models Using lme4." Journal of Statistical Software (2015). <https://doi.org/10.18637/jss.v067.i01>`_
