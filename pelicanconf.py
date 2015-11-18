#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'LukasWoodtli'
SITENAME = u'Rezepte'
SITEURL = 'http://lukaswoodtli.github.io/Rezepte'

PATH = 'content'

TIMEZONE = 'Europe/Zurich'

DEFAULT_LANG = u'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

MD_EXTENSIONS = ['extra', 'sane_lists', 'toc', 'footnotes']

DOCUTILS_SETTINGS = {'table_style' : 'borderless'} # 'math_output': 'mathjax'

THEME = "pelican-chameleon"

