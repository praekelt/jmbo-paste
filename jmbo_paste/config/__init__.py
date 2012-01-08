from os import path

SCRIPT_PATH =  path.abspath(path.dirname(__file__))

APP_CONFIG = {
        'django-category': {
            'module_name': 'category',
            'installed_app_dependencies': ['south'],
            'confirm': False,
        },
        'django-ckeditor': {
            'module_name': 'ckeditor',
            'urlconf_additions': '%s/ckeditor_urlconf_additions' % SCRIPT_PATH,
            'buildout_media_links': ('django-ckeditor://ckeditor/media/ckeditor',),
            'settings': (
                "# URL prefix for ckeditor JS and CSS media (not uploaded media). Make sure to use a trailing slash.\nCKEDITOR_MEDIA_PREFIX = '/media/ckeditor/'",
                "# Specify absolute path to your ckeditor media upload directory.\n# Make sure you have write permissions for the path, i.e/home/media/media.lawrence.com/uploads/\nCKEDITOR_UPLOAD_PATH = '%s/media/uploads/' % BUILDOUT_PATH",
            ),
        },
        'django-export': {
            'module_name': 'export',
            'installed_app_dependencies': ['django-object-tools',]
        },
        'django-generate': {
            'module_name': 'generate',
        },
        'django-gizmo': {
            'module_name': 'gizmo', 
            'settings': (
                "# Module containing gizmo configuration\nROOT_GIZMOCONF = '%s.gizmos' % PROJECT_MODULE",
            ),
        },
        'django-googlesearch': {
            'module_name': 'googlesearch',
            'urlconf_additions': '%s/googlesearch_urlconf_additions' % SCRIPT_PATH,
        },
        'django-likes': {
            'module_name': 'likes',
            'middleware_classes': ('likes.middleware.SecretBallotUserIpUseragentMiddleware',),
            'urlconf_additions': '%s/likes_urlconf_additions' % SCRIPT_PATH,
            'buildout_media_links': ('django-likes://likes/media/likes',),
            'installed_app_dependencies': ['django-secretballot',],
            'skip_setup_py': True,
        },
        'django-object-tools': {
            'module_name': 'object_tools',
            'urlconf_additions': '%s/object_tools_urlconf_additions' % SCRIPT_PATH,
        },
        'django-photologue': {
            'module_name': 'photologue',         
            'skip_setup_py': True,
        },
        'django-preferences': {
            'module_name': 'preferences',
            'template_context_processor_additions': ('preferences.context_processors.preferences_cp',),
        },
        # XXX: django-profile namespace needs to be updated to avoid confilct with python-profile package. 
        #'django-profile': { 
        #    'module_name': 'profile', 
        #    'model_additions': '%s/profile_model_additions.py' % SCRIPT_PATH,
        #    'settings': (
        #        "# The site-specific user profile model used by this site.\nAUTH_PROFILE_MODULE = '%s.Profile' % PROJECT_MODULE",
        #    )
        #},
        'django-publisher': {
            'module_name': 'publisher',
            'confirm': False,
        },
        'django-recaptcha': {
            'module_name': 'captcha',
        },
        'django-registration': {
            'module_name': 'registration', 
            'find_links': ('https://bitbucket.org/ubernostrum/django-registration/downloads/django-registration-0.8-alpha-1.tar.gz#egg=django-registration-0.8-alpha-1',),
        },
        'django-richcomments': {
            'module_name': 'richcomments',
            'urlconf_additions': '%s/richcomments_urlconf_additions' % SCRIPT_PATH,
            'buildout_media_links': ('django-richcomments://richcomments/media/richcomments',),
        },
        'django-secretballot': {
            'module_name': 'secretballot', 
            'confirm': False,
        },
        'django-section': {
            'module_name': 'section',
        },
        'django-snippetscream': {
            'module_name': 'snippetscream',
        },
        'jmbo': {
            'module_name': 'jmbo',
            'installed_app_dependencies': ['django-category', 'django-publisher', 'django-likes'],
        },
        'jmbo-banner': {
            'module_name': 'banner',
        },
        'jmbo-calendar': {
            'module_name': 'cal', 
        },
        'jmbo-chart': {
            'module_name': 'chart', 
            'urlconf_additions': '%s/chart_urlconf_additions' % SCRIPT_PATH,
        },
        'jmbo-competition': {
            'module_name': 'competition',
            'urlconf_additions': '%s/competition_urlconf_additions' % SCRIPT_PATH,
        },
        'jmbo-contact': {
            'module_name': 'contact',
            'urlconf_additions': '%s/contact_urlconf_additions' % SCRIPT_PATH,
        },
        'jmbo-event': {
            'module_name': 'event', 
            'urlconf_additions': '%s/event_urlconf_additions' % SCRIPT_PATH,
        },
        'jmbo-gallery': {
            'module_name': 'gallery',
            'urlconf_additions': '%s/gallery_urlconf_additions' % SCRIPT_PATH,
        },
        'jmbo-foundry': {
            'module_name': 'foundry',
            'middleware_classes': ('foundry.middleware.AgeGateway', 'foundry.middleware.VerboseRequestMeta'),
            'urlconf_additions': '%s/foundry_urlconf_additions' % SCRIPT_PATH,
            'installed_app_dependencies': ['django-preferences', 'django-snippetscream','south'],
            'template_loaders_additions': ('foundry.loaders.TypeLoader',),
            'settings': ('TEMPLATE_TYPE = "basic"',),
        },
        'jmbo-music': {
            'module_name': 'music', 
            'urlconf_additions': '%s/music_urlconf_additions' % SCRIPT_PATH,
            'settings': (
                "# API key if you are going to make use of LastFM\nLASTFM_API_KEY = ''",
            ),

        },
        'jmbo-post': {
            'module_name': 'post', 
        },
        'jmbo-show': {
            'module_name': 'show', 
            'urlconf_additions': '%s/show_urlconf_additions' % SCRIPT_PATH,
        },
        'jmbo-social': {
            'module_name': 'social', 
        },
    }
