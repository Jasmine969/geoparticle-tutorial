# Configuration file for the Sphinx documentation builder.

# -- Project information
import sys
import os

# 确保路径正确
sys.path.insert(0, os.path.abspath('../..'))

project = 'geoparticle-documentation'
copyright = '2025, Hong Zhu'
author = 'Hong Zhu'

release = '1.0.2'
version = '1.0.2'

# -- General configuration

extensions = [
    'sphinx.ext.autodoc',  # 重新启用autodoc
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'autoapi.extension',   # 保留autoapi但调整配置
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

# AutoAPI配置 - 简化并修复
autoapi_type = 'python'
autoapi_dirs = ['../../geoparticle']
autoapi_root = 'autoapi'
autoapi_options = [
    'members',
    'show-inheritance',
    'show-module-summary',
    'special-members',
]
autoapi_add_toctree_entry = False  # 禁用自动toctree
autoapi_keep_files = False

# 重要的修复：添加忽略模式
autoapi_ignore = []  # 确保没有忽略任何文件

# Autodoc配置（备用）
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': False,
    'show-inheritance': True,
}

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True

# 确保Python路径正确
python_path = os.path.abspath('../..')
if python_path not in sys.path:
    sys.path.insert(0, python_path)