#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Markus'
SITENAME = 'markusgoller.at'
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
THEME='../../pelican_themes/attila_msvalina'
HOME_COVER = 'pages/images/dreizinnen_wanderung_nik.JPG'

# Theme
#THEME='../../pelican_themes/pelican-clean-blog'
#HEADER_COVER = 'pages/images/dreizinnen_wanderung_nik.JPG'

# Theme
#THEME='../../pelican_themes/attila_arulrajnet'
#HEADER_COLOR =  'green'
#HEADER_COVER = 'images/elenabsl_shutterstock.jpg'
#HOME_COVER = 'https://casper.ghost.org/v1.0.0/images/welcome.jpg'
#HOME_COVER = 'https://github.com/arulrajnet/attila/blob/master/static/images/post-bg.jpg'


# Theme Does not work
#HOME_COVER = '/home/unix/anaconda3/envs/pelican/lib/python3.8/site-packages/pelican/themes/attila/static/images/home-bg.jpg'
#HEADER_COVER = 'static/my_image.png'
#HOME_COVER = '/home/unix/Downloads/remote_kaese.jpg'
#HOME_COVER = 'https://extrajournal.net/subwpd/wp-content/uploads/2019/11/VW-ID.-Space-Vizzion-Credit-Volkswagen-AG.jpg'



