# Configuration file for the Sphinx documentation builder.

# -- Project information
import sys
import os

sys.path.insert(0, os.path.abspath('../..'))

project = 'geoparticle-documentation'
copyright = '2025, Hong Zhu'
author = 'Hong Zhu'

release = '1.0.2'
version = '1.0.2'

# -- General configuration

extensions = [
    # 'sphinx.ext.duration',
    # 'sphinx.ext.doctest',
    # 'sphinx.ext.autodoc',
    # 'sphinx.ext.autosummary',
    # 'sphinx.ext.intersphinx',
    # 'sphinx.ext.napoleon',
    # 'sphinx.ext.viewcode'
    'autoapi.extension',
    'sphinx.ext.napoleon',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# autodoc_default_options = {
#     'members': True,                    # display all members
#     'member-order': 'bysource',         # order members by source order
#     'special-members': '__init__',      # display __init__
#     'undoc-members': False,             # hide undocumented members
#     'show-inheritance': True,
# }
#
# napoleon_google_docstring = True
# napoleon_numpy_docstring = True
# napoleon_include_init_with_doc = True
# napoleon_include_private_with_doc = True
# napoleon_include_special_with_doc = True
#
# autoclass_content = 'both'
autoapi_type = 'python'
autoapi_dirs = ['../../geoparticle']  # 指向你的包目录
autoapi_root = 'autoapi'
autoapi_options = [
    'members',
    'undoc-members',
    'show-inheritance',
    'show-module-summary',
    'special-members',
    'imported-members',
]
# 添加这些重要的autoapi配置
autoapi_add_toctree_entry = True
autoapi_keep_files = False
autoapi_add_objects_to_toctree = True
autoapi_python_use_implicit_namespaces = False

# Napoleon配置（用于解析docstring）
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_keyword = True
napoleon_custom_sections = None

# 确保Python能够找到你的模块
python_use_unqualified_type_names = True
# 禁用标准的autodoc，避免重复
autodoc_typehints = 'none'