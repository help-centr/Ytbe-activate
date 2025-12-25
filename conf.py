# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Yt.be/activate – YouTube TV Activation Guide'
copyright = '2025, YouTube Activation Guide'
author = 'YouTube Activation Support Team'

release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Allow raw HTML blocks in rst
raw_enabled = True

# -- HTML output -------------------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_title = "Yt.be/activate – Activate YouTube on Smart TV & Streaming Devices"
html_short_title = "Yt.be/activate Guide"

# Favicon (place favicon.ico inside _static folder)
html_favicon = '_static/favicon.ico'

html_static_path = ['_static']

# Hide source link
html_show_sourcelink = False

# Theme customization
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'show_powered_by': False,
}

# Allow unsafe HTML (for embeds, buttons, CTA)
html_allow_unsafe = True
