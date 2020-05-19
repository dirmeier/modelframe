#!/usr/bin/env python3

import os
import sys

sys.path.insert(0, os.path.abspath('../../'))

extensions = ['jupyter_sphinx',
              'sphinx.ext.autodoc',
              'sphinx.ext.mathjax',
              'sphinx.ext.viewcode',
              'sphinxcontrib.fulltoc',
              'sphinx_fontawesome',
              'nbsphinx']
templates_path = ['_templates']
suppress_warnings = ['image.nonlocal_uri']

source_suffix = '.rst'
master_doc = 'index'

project = 'modelframe'
copyright = '2020, Simon Dirmeier'
author = 'Simon Dirmeier'

language = None

exclude_patterns = []

pygments_style = 'sphinx'
todo_include_todos = False

html_show_sourcelink = False
html_show_sphinx = False

html_theme = 'alabaster'
html_theme_options = {
    'show_powered_by': False,
    'github_user': 'dirmeier',
    'note_bg': '#FFF59C',
    'sidebarwidth': 5
}
html_sidebars = {
    'index': ['localtoc.html']
}
html_title = ""
html_static_path = ['_static']
htmlhelp_basename = 'modelframedoc'


def setup(app):
    app.add_stylesheet('custom.css')
