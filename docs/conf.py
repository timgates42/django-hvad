# -*- coding: utf-8 -*-
#
# Project 何 documentation build configuration file, created by
# sphinx-quickstart on Tue Feb 15 11:19:28 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os, sphinx

readthedocs = os.environ.get('READTHEDOCS', None) == 'True'

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

sys.path.extend((
    os.path.abspath(os.path.join(os.path.dirname(__file__), '_ext')),
))

# -- General configuration -----------------------------------------------------

extensions = [
    'sphinx.ext.intersphinx',
    'djangodocs',
    'github'
]
intersphinx_mapping = {
    'python': ('http://docs.python.org/2.7', None),
    'django': ('http://readthedocs.org/docs/django/en/latest/', None),
}

templates_path = ['_templates']
source_suffix = '.rst'
exclude_patterns = ['_build']
master_doc = 'index'

# General information about the project.
project = u'django-hvad'
copyright = u'2011-2015, Kristian Øllegaard, Jonas Obrist & contributors'

version = '1.5'
release = '1.5.1'


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'trac'

# -- Options for HTML output ---------------------------------------------------

if sphinx.version_info >= (1, 3):
    html_theme = 'default' if readthedocs else 'classic'
else:
    html_theme = 'default'
html_theme_options = {
    'externalrefs': True,
}

html_style = 'stylesheet.css'
html_static_path = ['_static']

html_use_smartypants = True
html_show_sourcelink = False

# Custom sidebar templates, maps document names to template names.
html_sidebars = {'**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html']}


# Output file base name for HTML help builder.
htmlhelp_basename = 'Projectdoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'Project.tex', u'Django Hvad Documentation',
   u'Jonas Obrist & contributors', 'manual'),
]


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'project', u'Django Hvad Documentation',
     [u'Kristian Øllegaard, Jonas Obrist & contributors'], 1)
]

# -- Options for local extensions ----------------------------------------------

github_owner = 'KristianOellegaard'
github_repo = 'django-hvad'

