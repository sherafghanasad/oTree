import os
from os import environ
import dj_database_url
from boto.mturk import qualification

import otree.settings


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

mturk_hit_settings = {
    'keywords': ['bonus', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24, # 7 days
    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': [
    {
        'QualificationTypeId': "00000000000000000071",
        'Comparator': "EqualTo",
        'LocaleValues': [{'Country': "US"}]
    },
    ]
}

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}

SESSION_CONFIGS = [
    # {
    #     'name': 'public_goods',
    #     'display_name': "Public Goods",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['public_goods', 'payment_info'],
    # },
    # {
    #     'name': 'guess_two_thirds',
    #     'display_name': "Guess 2/3 of the Average",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['guess_two_thirds', 'payment_info'],
    # },
    # {
    #     'name': 'survey',
    #     'display_name': "Survey",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['survey', 'payment_info'],
    # },
    # {
    #     'name': 'quiz',
    #     'display_name': "Quiz",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['quiz'],
    # },
    # {
    #     'name': 'my_simple_survey',
    #     'display_name': "My Simple Survey",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['my_simple_survey'],
    # },
    # {
    #     'name': 'my_public_goods',
    #     'display_name': "My Public Goods (Simple Version)",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['my_public_goods'],
    #     'use_browser_bots': False
    # },
    # {
    # 'name': 'my_trust',
    # 'display_name': "My Trust Game (simple version from tutorial)",
    # 'num_demo_participants': 2,
    # 'app_sequence': ['my_trust'],
    # },
    # {
    # 'name': 'my_matching_pennies',
    # 'display_name': "My Matching Pennies (tutorial version)",
    # 'num_demo_participants': 2,
    # 'app_sequence': [
    #     'my_matching_pennies',
    # ],
    # },
    # {
    # 'name': 'gift_exchange',
    # 'display_name': "Gift Exchange Game",
    # 'num_demo_participants': 6,
    # 'app_sequence': ['gift_exchange'],
    # },
    {
    'name': 'demographic_survey',
    'display_name': "Demographic Survey",
    'num_demo_participants': 6,
    'app_sequence': ['demographic_survey'],
    },
    {
    'name': 'experiment',
    'display_name': "Experiment",
    'num_demo_participants': 4,
    'app_sequence': ['experiment'],
    },
    # {
    # 'name': 'experiment_grouping',
    # 'display_name': "Experiment Grouping",
    # 'num_demo_participants': 4,
    # 'app_sequence': ['experiment_grouping', 'experiment'],
    # },
    # other session configs go here ...
]



# see the end of this file for the inactive session configs


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = [
    {
        'name': 'econ101',
        'display_name': 'Econ 101 class',
        'participant_label_file': '_rooms/econ101.txt',
    },
    {
        'name': 'live_demo',
        'display_name': 'Room for live demo (no participant labels)',
    },
    {
        'name': 'experiment',
        'display_name': 'Experiment',
    },
    {
        'name': 'demographic_survey',
        'display_name': 'Demographic Survey',
    },

]


# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')

# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

SENTRY_DSN = environ.get('SENTRY_DSN')

DEMO_PAGE_INTRO_HTML = """

<ul>
    <li>
        <a href="https://github.com/oTree-org/otree" target="_blank">
            oTree on GitHub
        </a>.
    </li>
    <li>
        <a href="http://www.otree.org/" target="_blank">
            oTree homepage
        </a>.
    </li>
</ul>
<p>
    Here are various games implemented with oTree. These games are all open
    source, and you can modify them as you wish.
</p>
"""

# don't share this with anybody.
SECRET_KEY = 'f*n_(%11(w&438tavghijhaaze8=#st#j#o8z1#alv8aq2&r)y'


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# STATIC_URL = '/static/'

# MIDDLEWARE_CLASSES = (
#     # Simplified static file serving.
#     # https://warehouse.python.org/project/whitenoise/
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     # ...
# )

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DATABASES = {
    'default': dj_database_url.config(
        # Rather than hardcoding the DB parameters here,
        # it's recommended to set the DATABASE_URL environment variable.
        # This will allow you to use SQLite locally, and postgres/mysql
        # on the server
        # Examples:
        # export DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
        # export DATABASE_URL=mysql://USER:PASSWORD@HOST:PORT/NAME

        # fall back to SQLite if the DATABASE_URL env var is missing
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}


# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree',
                  'otree_tools',
                  # 'django.contrib.staticfiles'
                  ]
# inactive session configs
### {
###     'name': 'trust',
###     'display_name': "Trust Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['trust', 'payment_info'],
### },
### {
###     'name': 'prisoner',
###     'display_name': "Prisoner's Dilemma",
###     'num_demo_participants': 2,
###     'app_sequence': ['prisoner', 'payment_info'],
### },
### {
###     'name': 'ultimatum',
###     'display_name': "Ultimatum (randomized: strategy vs. direct response)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
### },
### {
###     'name': 'ultimatum_strategy',
###     'display_name': "Ultimatum (strategy method treatment)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
###     'use_strategy_method': True,
### },
### {
###     'name': 'ultimatum_non_strategy',
###     'display_name': "Ultimatum (direct response treatment)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
###     'use_strategy_method': False,
### },
### {
###     'name': 'vickrey_auction',
###     'display_name': "Vickrey Auction",
###     'num_demo_participants': 3,
###     'app_sequence': ['vickrey_auction', 'payment_info'],
### },
### {
###     'name': 'volunteer_dilemma',
###     'display_name': "Volunteer's Dilemma",
###     'num_demo_participants': 3,
###     'app_sequence': ['volunteer_dilemma', 'payment_info'],
### },
### {
###     'name': 'cournot',
###     'display_name': "Cournot Competition",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'cournot', 'payment_info'
###     ],
### },
### {
###     'name': 'principal_agent',
###     'display_name': "Principal Agent",
###     'num_demo_participants': 2,
###     'app_sequence': ['principal_agent', 'payment_info'],
### },
### {
###     'name': 'dictator',
###     'display_name': "Dictator Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['dictator', 'payment_info'],
### },
### {
###     'name': 'matching_pennies',
###     'display_name': "Matching Pennies",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'matching_pennies',
###     ],
### },
### {
###     'name': 'traveler_dilemma',
###     'display_name': "Traveler's Dilemma",
###     'num_demo_participants': 2,
###     'app_sequence': ['traveler_dilemma', 'payment_info'],
### },
### {
###     'name': 'bargaining',
###     'display_name': "Bargaining Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['bargaining', 'payment_info'],
### },
### {
###     'name': 'common_value_auction',
###     'display_name': "Common Value Auction",
###     'num_demo_participants': 3,
###     'app_sequence': ['common_value_auction', 'payment_info'],
### },
### {
###     'name': 'bertrand',
###     'display_name': "Bertrand Competition",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'bertrand', 'payment_info'
###     ],
### },
### {
###     'name': 'real_effort',
###     'display_name': "Real-effort transcription task",
###     'num_demo_participants': 1,
###     'app_sequence': [
###         'real_effort',
###     ],
### },
### {
###     'name': 'lemon_market',
###     'display_name': "Lemon Market Game",
###     'num_demo_participants': 3,
###     'app_sequence': [
###         'lemon_market', 'payment_info'
###     ],
### },
### {
###     'name': 'public_goods_simple',
###     'display_name': "Public Goods (simple version from tutorial)",
###     'num_demo_participants': 3,
###     'app_sequence': ['public_goods_simple', 'payment_info'],
### },
### {
###     'name': 'trust_simple',
###     'display_name': "Trust Game (simple version from tutorial)",
###     'num_demo_participants': 2,
###     'app_sequence': ['trust_simple'],
### },


otree.settings.augment_settings(globals())
