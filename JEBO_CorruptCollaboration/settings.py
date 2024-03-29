from os import environ

SESSION_CONFIGS = [
    dict(
        name='simultaneous',
        app_sequence=['simu_S1','simu_S2','simu_S3'],  
        num_demo_participants=None,
        # use_browser_bots=True
    ),    
    dict(
        name='partially_sequential',
        app_sequence=['parse_S1','parse_S2','parse_S3'], 
        num_demo_participants=None,
        # use_browser_bots=True
    ),  
    dict(
        name='fully_sequential',
        app_sequence=['fuse_S1','fuse_S2','fuse_S3'], 
        num_demo_participants=None,
        # use_browser_bots=True
    ),  
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['app_payoffs','guess_results']
SESSION_FIELDS = ['GroupStructure']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '1565152346369'
