# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Dynart Documentation'
copyright = '2025, Dynart'
author = 'Dynart'
release = '0.0.0-2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

myst_enable_extensions = [
    "attrs_inline",   # IDs after inline content:  ## Title {#id}
    "attrs_block",    # IDs before a block:       {#id}\n## Title
    "linkify",        # https://xyz.com to links
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "myst",
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_logo = '_static/dynart-logo.svg'

pygments_style = 'dracula'