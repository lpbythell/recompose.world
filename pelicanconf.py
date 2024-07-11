# pelicanconf.py
AUTHOR = 'Louis Alderson-Bythell'
<<<<<<< HEAD
SITENAME = 'Recompose'
=======
SITENAME = 'Recompose World'
>>>>>>> 1390e6e (Initial commit with Solar theme, plugins, and content)
SITEURL = 'https://recompose.world'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Theme
<<<<<<< HEAD
THEME = 'path_to_solar_theme'  # Ensure this points to the solar theme directory

# Plugins
PLUGIN_PATHS = ['solar-plugins']
PLUGINS = ['plugin1', 'plugin2']  # Replace 'plugin1', 'plugin2' with actual plugin names
=======
THEME = 'solar'  # Ensure this points to the solar theme directory

# Plugins
PLUGIN_PATHS = ['solar-plugins']
PLUGINS = ['neighbors', 'related_posts', 'addressable_paragraphs', 'dither', 'page_metadata', 'representative_image']
>>>>>>> 1390e6e (Initial commit with Solar theme, plugins, and content)

# GitHub Pages output path
OUTPUT_PATH = 'docs/'
