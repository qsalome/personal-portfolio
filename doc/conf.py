# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Personal portfolio'
copyright = 'Quentin Salomé'
author = 'Quentin Salomé'
release = '0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser','nbsphinx']

#nbsphinx_execute = 'always'
nbsphinx_execute = 'auto'  # Execute by default, but respect notebook metadata

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_last_updated_fmt = "%d %B %Y"
#html_logo = "static/logo/AutoGIS.PNG"
#html_favicon = 'static/logo/favicon.ico'
#html_short_title = "AutoGIS"
#html_title = ""

html_theme = "sphinx_book_theme"
#html_sidebars = {
#    '**': [
#        'navbar-logo.html'
#        'icon-links.html',
#        'sbt-sidebar-nav.html'
#    ]
#}

#html_theme_options = {
#    "home_page_in_toc": True,
#    "collapse_navigation": False,
#    'search_bar_position': 'none',
#    'nosidebar': True,
#    "launch_buttons": {
#        "binderhub_url": "https://mybinder.org",
#        "notebook_interface": "classic"
#    },
#    "use_edit_page_button": True,
#    "use_repository_button": True,
#    'logo_only': True,
#    'display_version': False,
#}

#html_static_path = ['static']


