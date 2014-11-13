#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import hashlib

# Jinja2 filter for generate md5 checksum
def md5filter(value):
    v = hashlib.md5()
    v.update(value)
    return v.hexdigest()

def formatDate(value):
    if 4 <= value.day <= 20 or 24 <= value.day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][value.day % 10 - 1]

    format = str(value.day) + suffix + ' of %B %Y'

    return value.strftime(format)

JINJA_FILTERS = {'md5': md5filter, 'format_date': formatDate}
DISPLAY_CATEGORIES_ON_MENU = False
TYPOGRIFY = False

AUTHOR = u'cristian'
AUTHOR_FULLNAME = u'Cristian Prieto'
SITENAME = u'IDisposable Thoughts'
SITEURL = ''
SITESUBTITLE = u"Where's my coding t-shirt?"
EMAIL = u'me@cprieto.com'

THEME = u'themes/less'

PATH = 'content'

TIMEZONE = 'Australia/Melbourne'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['extra', 'extra/favicon.ico', 'extra/favicon.png']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon.png': {'path': 'favicon.png'}
}
FAVICON_TYPES = ['ico','png']

DIRECT_TEMPLATES = ('index', 'categories', 'archives')

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}.html'
