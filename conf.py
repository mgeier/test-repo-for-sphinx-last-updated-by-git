import os
import sys

sys.path.insert(0, os.path.abspath('.'))

html_theme = 'classic'
html_show_copyright = False
extensions = [
    'sphinx.ext.autosummary',
    'sphinx_last_updated_by_git',
]

autosummary_generate = ['api']

html_last_updated_fmt = '%Y-%m-%d %H:%M:%S'

# Remove this if you want to see the contents of the docs:
templates_path = ['_templates']
