# from datetime import datetime

# AUTHOR = "Thomas Schuster"
# SITEURL = "http://localhost:8000"
# SITENAME = "Thomas Schuster"
# SITETITLE = "Thomas Schuster"
# #SITESUBTITLE = "The minimalist Pelican theme"
# SITEDESCRIPTION = "Thomas Schuster's website"
# # SITELOGO = ''
# # FAVICON = '/images/favicon.ico'
# #BROWSER_COLOR = "#333333"
# #PYGMENTS_STYLE = "monokai"

# #ROBOTS = "index, follow"

# #THEME = "../"
# PATH = "content"
# OUTPUT_PATH = "blog/"
# TIMEZONE = "America/Los_Angeles"

# # PLUGIN_PATHS = ['pelican-plugins']

# # PLUGINS = ['i18n_subsites']

# # JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# I18N_TEMPLATES_LANG = "en"
# DEFAULT_LANG = "en"
# OG_LOCALE = "en_US"
# LOCALE = "en_US"

# DATE_FORMATS = {
#     "en": "%B %d, %Y",
# }

# FEED_ALL_ATOM = "feeds/all.atom.xml"
# CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None

# # USE_FOLDER_AS_CATEGORY = False
# # MAIN_MENU = True
# # HOME_HIDE_TAGS = True

# # SOCIAL = (
# #     ("LinkedIn", "https://www.linkedin.com/in/thomas-schuster-b27b0a13b/"),
# #     ("Google Scholar", "https://scholar.google.com/citations?hl=en&view_op=list_works&gmla=AJsN-F5vSKFiJs8roazFNrt9c9RtFVh_U3e3Gfodn5Ot4Zi7CLDSH-2v5uZQUctlZ2fnuXLvMUeTwe7Fy10sPoYi_MoeoLGL9jiKcs8Fba8ohJvEIl-hDtL7L1mJKGt0sWMCzdmqRDWkjvuL0CZtnWwqCq_UAVslEg&user=_lxZu14AAAAJ"),
# # )

# # MENUITEMS = (
# #     ("Archives", "/archives.html"),
# #     ("Categories", "/categories.html"),
# #     ("Tags", "/tags.html"),
# # )

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa",
}

# COPYRIGHT_YEAR = datetime.now().year
# DEFAULT_PAGINATION = 10

# # DISQUS_SITENAME = "flex-pelican"
# # ADD_THIS_ID = "ra-55adbb025d4f7e55"

# #STATIC_PATHS = ["images", "extra/ads.txt", "extra/CNAME"]
# STATIC_PATHS = ["images"]

# # EXTRA_PATH_METADATA = {
# #     "extra/ads.txt": {"path": "ads.txt"},
# #     "extra/CNAME": {"path": "CNAME"},
# # }

# # THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
# # THEME_COLOR_ENABLE_USER_OVERRIDE = True

# # USE_LESS = True

# # GOOGLE ANALYTICS
# # For Google Analytics 4 use. Note that for old Google Analytics ('UA-XXXXX') the GOOGLE_ANALYTICS variable is included in publishconfig.py
# # GOOGLE_GLOBAL_SITE_TAG = 'G-XXXXX'

# #!/usr/bin/env python
# # -*- coding: utf-8 -*- #

AUTHOR = "Thomas Schuster"
SITEURL = "tsschuster.github.io"
SITENAME = "Thomas Schuster"
SITETITLE = "About"
#SITESUBTITLE = "The minimalist Pelican theme"
SITEDESCRIPTION = "Thomas Schuster's website"
FAVICON = '/images/lone_molecule.png'
SITELOGO = '/images/profile_pic.png'
# HOMETITLE = 'about'

PATH = 'content'
THEME = 'Flex'

STATIC_PATHS = ['images','pdfs']

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# CC_LICENSE = {
#     "name": "GNU General Public License",
#     "version": "3.0"
# }

# Blogroll

# SOCIAL = (
#     ("LinkedIn", "https://www.linkedin.com/in/thomas-schuster-b27b0a13b/"),
#     ("Google Scholar", "https://scholar.google.com/citations?hl=en&view_op=list_works&gmla=AJsN-F5vSKFiJs8roazFNrt9c9RtFVh_U3e3Gfodn5Ot4Zi7CLDSH-2v5uZQUctlZ2fnuXLvMUeTwe7Fy10sPoYi_MoeoLGL9jiKcs8Fba8ohJvEIl-hDtL7L1mJKGt0sWMCzdmqRDWkjvuL0CZtnWwqCq_UAVslEg&user=_lxZu14AAAAJ"),
# )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True