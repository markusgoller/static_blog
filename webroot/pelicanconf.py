#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Markus'
SITENAME = 'markusgoller'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = True
SOCIAL = (('github', 'https://github.com/markusgoller'),
          #('linkedin','https://www.linkedin.com/in/markus-goller-ab975317a/')
          )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME='../pelican_themes/attila_msvalina'
#THEME='../pelican_themes/attila'
#THEME='../pelican_themes/attila_newest'
# Code highlights
#COLOR_SCHEME_CSS = 'github.css'

#Cover
#HOME_COVER = 'images/dreizinnen_wanderung_nik.JPG'
#HOME_COVER = 'images/PSX_20200814_222100.jpg'
HOME_COVER = 'images/IMG_20200819_130938_resize.jpg'

AUTHORS_BIO = {
  "markus": {
    "name": "Markus",
    "bio": "Open Source Lover",   # Example: Systems Architect. Taco lover. Husband. Dog owner.
    #"linkedin": "markus-goller-ab975317a/",
    "github": "markusgoller",
  }
}

MENUITEMS = [('Home', '/'), ('Archives', '/archives.html')]

# Including pelican-jupyter
# https://github.com/danielfrg/pelican-jupyter
MARKUP = ('md', )
from pelican_jupyter import liquid as nb_liquid
PLUGINS = [nb_liquid]
IGNORE_FILES = [".ipynb_checkpoints"]

# # Markdown customization
# MARKDOWN = {
#     'extension_configs': {
#         'markdown.extensions.codehilite': {
#             'css_class': 'highlight',
#             'guess_lang': False,
#         },
#         'markdown.extensions.extra': {},
#         'markdown.extensions.meta': {},
#         'markdown.extensions.toc': {
#             'anchorlink': True,
#             'title': 'Contents',
#         },
#         'markdown.extensions.sane_lists': {},
#     },
#     'output_format': 'html5',
# }

# # Pelican plugins
# PLUGIN_PATHS = ['../pelican-plugins']


