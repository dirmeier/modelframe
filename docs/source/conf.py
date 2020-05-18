#!/usr/bin/env python3

import sys
import os

sys.path.append( os.path.abspath('../../'))
extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']
source_suffix = '.rst'
#source_encoding = 'utf-8-sig'
master_doc = 'index'

project = 'modelframe'
author = 'Simon Dirmeier'

version = '0.2'
release = '0.2'

language = None
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'alabaster'

htmlhelp_basename = 'modelframedoc'

latex_elements = {}
latex_documents = [
  (master_doc, 'modelframe.tex', 'modelframe Documentation',
   'Simon Dirmeier', 'manual'),
]
man_pages = [
    (master_doc, 'modelframe', 'modelframe Documentation',
     [author], 1)
]
texinfo_documents = [
  (master_doc, 'modelframe', 'modelframe Documentation',
   author, 'modelframe', 'One line description of project.',
   'Miscellaneous'),
]
