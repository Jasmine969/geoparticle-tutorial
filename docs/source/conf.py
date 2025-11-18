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
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
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

autodoc_default_options = {
    'members': True,                    # display all members
    'member-order': 'bysource',         # order members by source order
    # 'special-members': '__init__',      # display __init__
    'undoc-members': False,             # hide undocumented members
    'private-members': False,           # 不显示私有成员
    'show-inheritance': True,
    'exclude-members': '__weakref__',  # 排除一些不需要的成员
}

autoclass_content = 'class'  # 只显示类文档字符串，不显示__init__文档
# 控制automodule的行为
autosummary_generate = True  # 为autosummary指令生成stub文件
autosummary_imported_members = False

# Napoleon配置（用于解析Google/NumPy风格的docstring）
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False  # 关键：不在类文档中重复显示__init__
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_keyword = True

# 其他配置
add_module_names = False  # 简化全限定名显示
modindex_common_prefix = ['geoparticle.']