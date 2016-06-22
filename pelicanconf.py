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
PAGINATION_PATTERNS = ( (1, '{base_name}/', '{base_name}/index.html'), (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'), )

MD_EXTENSIONS = ['extra', 'sane_lists', 'toc', 'footnotes']

DOCUTILS_SETTINGS = {'table_style' : 'borderless'} # 'math_output': 'mathjax'

THEME = "blue-penguin"


TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'
CATEGORY_URL = 'category/{slug}/' 
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_URL = 'categories/'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = 'archives/index.html'

# Keep the generated blog index but save it under different name
#INDEX_SAVE_AS = 'blog_index.html'

DISPLAY_PAGES_ON_MENU = True

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    ('Tags', TAGS_URL, TAGS_SAVE_AS),
    ('Kategorien', CATEGORIES_URL, CATEGORIES_SAVE_AS),
    ('Alle', ARCHIVES_URL, ARCHIVES_SAVE_AS),
)

