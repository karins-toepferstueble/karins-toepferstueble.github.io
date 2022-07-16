#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'karin'
SITENAME = 'Karins Töpferstube'
SITEURL = 'https://karins-töpferstube.de'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'de'

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_ATOM = ''
# FEED_ALL_RSS = 'feeds/all.rss.xml'
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None

# Social widget
# SOCIAL = (
#     ('twitter', 'https://twitter.com/EsslingenMaker'),
#     ('github', 'https://github.com/Makerspace-Esslingen'),
#     ('instagram', 'https://instagram.com/esslingenmaker'),
# )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "themes/Peli-Kiera"

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (
    ('Produkte', '/pages/produkte.html'),
    ('Produktinformationen', '/pages/produktinformationen.html'),
    ('Über mich', '/pages/uber-mich.html'),
    ('Kontakt', '/pages/kontakt.html'),
)

from pelican.settings import DEFAULT_CONFIG
from pelican.readers import MarkdownReader

config = DEFAULT_CONFIG.copy()

INTRO, _ = MarkdownReader(config).read("content/pages/landing.md")

CACHE_CONTENT=False
