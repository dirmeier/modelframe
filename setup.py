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


from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


test_deps = [
    'black',
    'coverage',
    'pytest>=3.6.2',
    'pytest-cov',
    'pytest-pep8',
    'flake8'
]

setup(
    name='modelframe',
    version='0.1.0',
    description='Compute fixed and random effects model matrices in Python',
    long_description=readme(),
    url='https://github.com/dirmeier/modelframe',
    download_url='https://github.com/dirmeier/modelframe/tarball/0.0.1',
    author='Simon Dirmeier',
    author_email='simon.dirmeier@web.de',
    license='GPLv3',
    keywords=['?'],
    packages=['modelframe'],
    include_package_data=True,
    install_requires=[
        'numpy',
        'scipy',
        'pandas'
    ],
    test_requires=test_deps,
    extras_require={
        'test': test_deps
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ]
)
