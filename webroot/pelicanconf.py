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
# Forked from orginal markusgoller/attilla
THEME='../../pelican_themes/attila'   
HOME_COVER = 'images/dreizinnen_wanderung_nik.JPG'
#HOME_COVER = 'images/IMG-20200726-WA0003.jpg'

# Theme
#THEME='../../pelican_themes/pelican-clean-blog'
#HEADER_COVER = 'pages/images/dreizinnen_wanderung_nik.JPG'

# Theme
#THEME='../../pelican_themes/attila_arulrajnet'
#HEADER_COLOR =  'green'
#HEADER_COVER = 'images/elenabsl_shutterstock.jpg'
#HOME_COVER = 'https://casper.ghost.org/v1.0.0/images/welcome.jpg'
#HOME_COVER = 'https://github.com/arulrajnet/attila/blob/master/static/images/post-bg.jpg'

AUTHORS_BIO = {
  "markus": {
    "name": "Markus",
    "bio": "Open Source Lover",   # Example: Systems Architect. Taco lover. Husband. Dog owner.
    #"linkedin": "markus-goller-ab975317a/",
    "github": "markusgoller",
  }
}

PLUGIN_PATHS = ['../../pelican-plugins']
PLUGINS = ['tipue_search']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search'))
MENUITEMS = [('Home', '/'), ('Archives', '/archives.html'), ('Search', '/search.html')]