from os import path

from paste.script import command
from paste.script.templates import Template, var
from random import choice

SCRIPT_PATH =  path.abspath(path.dirname(__file__))

APP_CONFIG = {
        'django-ckeditor': {
            'module_name': 'ckeditor',
            'urlconf_additions': '%s/config/ckeditor_urlconf_additions.py' % SCRIPT_PATH,
            'buildout_media_links': ('django-ckeditor://ckeditor/media/ckeditor',),
        },
        'django-generate': {
            'module_name': 'generate',
        },
        'django-gizmo': {
            'module_name': 'gizmo', 
        },
        'django-googlesearch': {
            'module_name': 'googlesearch',
            'urlconf_additions': '%s/config/googlesearch_urlconf_additions.py' % SCRIPT_PATH,
        },
        'django-likes': {
            'module_name': 'likes',
            'middleware_classes': ('likes.middleware.SecretBallotUserIpUseragentMiddleware',),
            'urlconf_additions': '%s/config/likes_urlconf_additions.py' % SCRIPT_PATH,
            'buildout_media_links': ('django-likes://likes/media/likes',),
            'installed_app_dependencies': ['secretballot',]
        },
        'django-preferences': {
            'module_name': 'preferences',
            'urlconf_additions': '%s/config/preferences_urlconf_additions' % SCRIPT_PATH,
            'template_context_processor_additions': ('preferences.context_processors.preferences_cp',),
        },
        'django-profile': { 
            'module_name': 'profile', 
            'model_additions': '%s/config/profile_model_additions.py' % SCRIPT_PATH,
        },
        'django-publisher': {
            'module_name': 'publisher',
        },
        'django-recaptcha': {
            'module_name': 'captcha',
        },
        'django-registration': {
            'module_name': 'registration', 
            'find_links': ('http://github.com/downloads/praekelt/public-eggs/django_registration-0.8_alpha_1-py2.6.egg#egg=django-registration',),
        },
        'django-richcomments': {
            'module_name': 'richcomments',
            'urlconf_additions': '%s/config/richcomments_urlconf_additions.py' % SCRIPT_PATH,
            'buildout_media_links': ('django-richcomments://richcomments/media/richcomments',),
        },
        'django-section': {
            'module_name': 'section',
        },
        'django-snippetscream': {
            'module_name': 'snippetscream',
        },
        'jmbo': {
            'module_name': 'jmbo',
            'urlconf_additions': '%s/config/jmbo_urlconf_additions.py' % SCRIPT_PATH,
            'installed_app_dependencies': ['category', 'photologue', 'publisher',]
        },
        'jmbo-banner': {
            'module_name': 'banner',
        },
        'jmbo-calendar': {
            'module_name': 'cal', 
        },
        'jmbo-chart': {
            'module_name': 'chart', 
            'urlconf_additions': '%s/config/chart_urlconf_additions.py' % SCRIPT_PATH,
        },
        'jmbo-competition': {
            'module_name': 'competition',
            'urlconf_additions': '%s/config/competition_urlconf_additions.py' % SCRIPT_PATH,
        },
        'jmbo-contact': {
            'module_name': 'contact',
            'urlconf_additions': '%s/config/contact_urlconf_additions.py' % SCRIPT_PATH,
        },
        'jmbo-event': {
            'module_name': 'event', 
            'urlconf_additions': '%s/config/event_urlconf_additions.py' % SCRIPT_PATH,
        },
        'jmbo-gallery': {
            'module_name': 'gallery',
            'urlconf_additions': '%s/config/gallery_urlconf_additions.py' % SCRIPT_PATH,
        },
        'jmbo-music': {
            'module_name': 'music', 
            'urlconf_additions': '%s/config/music_urlconf_additions.py' % SCRIPT_PATH,
        },
        'jmbo-post': {
            'module_name': 'post', 
        },
        'jmbo-show': {
            'module_name': 'show', 
            'urlconf_additions': '%s/config/show_urlconf_additions.py' % SCRIPT_PATH,
        },
        'jmbo-social': {
            'module_name': 'social', 
        },
    }

class JmboProjectTemplate(Template):
    _template_dir = 'templates/jmbo_project'
    summary = 'Creates a Buildout providing a Django instance and Django project with selected Jmbo apps installed.'
    use_cheetah = True

    vars = [
        var('secret_key', 'The secret key for hashing algorithms',
            default=''.join(
                [choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
            ) for i in range(50)])),
        var('hostname_prd', 'Production instance hostname', default='localhost'),
        var('hostname_staging', 'Staging instance hostname', default='localhost'),
        var('hostname_qa', 'Quality Assurance instance hostname', default='localhost'),
        var('hostname_dev', 'Development instance hostname', default='localhost'),
    ]

    def pre(self, command, output_dir, vars):
        vars['app_config'] = APP_CONFIG
        app_keys = APP_CONFIG.keys()
        app_keys.sort()
        for key in app_keys:
            vars[key] = command.challenge('Install %s?: y/n' % key, 'y', True)
            if key == 'django-recaptcha' and vars[key] == 'y':
                vars['app_config']['django-recaptcha']['public_key'] = command.challenge('Enter your Recaptcha Public Key: ', '', True)
                vars['app_config']['django-recaptcha']['private_key'] = command.challenge('Enter your Recaptcha Private Key: ', '', True)

        required_installed_apps = set()
        for key, value in vars.items():
            if value == 'y' and vars['app_config'].has_key(key):
                required_installed_apps.add(vars['app_config'][key]['module_name'])
                if vars['app_config'][key].has_key('installed_app_dependencies'):
                    for app in vars['app_config'][key]['installed_app_dependencies']:
                        required_installed_apps.add(app)

        vars['required_installed_apps'] = required_installed_apps
