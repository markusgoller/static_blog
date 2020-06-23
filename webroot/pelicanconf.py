#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Markus Goller'
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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME='../../pelican_themes/attila'
#HOME_COVER = '/home/unix/anaconda3/envs/pelican/lib/python3.8/site-packages/pelican/themes/attila/static/images/home-bg.jpg'
#HEADER_COVER = 'static/my_image.png'
#HOME_COVER = 'https://casper.ghost.org/v1.0.0/images/welcome.jpg'
#HOME_COVER = '/home/unix/Downloads/remote_kaese.jpg'
#HOME_COVER = 'https://extrajournal.net/subwpd/wp-content/uploads/2019/11/VW-ID.-Space-Vizzion-Credit-Volkswagen-AG.jpg'
HEADER_COLOR =  'green'
#A definition of a custom header cover is not possible

