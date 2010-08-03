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
        },
        'django-preferences': {
            'module_name': 'preferences',
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
            'find_links': ('https://github.com/downloads/praekelt/eggs/django_registration-0.8_alpha_1-py2.6.egg#egg=django-registration',),
        },
        'django-richcomments': {
            'module_name': 'richcomments',
            'urlconf_additions': '%s/config/richcomments_urlconf_additions.py' % SCRIPT_PATH,
            'buildout_media_links': ('django-richcomments://richcomments/media/richcomments',),
        },
        'django-section': {
            'module_name': 'section',
        },
        'panya': {
            'module_name': 'panya',
            'urlconf_additions': '%s/config/panya_urlconf_additions.py' % SCRIPT_PATH,
        },
        'panya-banner': {
            'module_name': 'banner',
        },
        'panya-calendar': {
            'module_name': 'cal', 
        },
        'panya-chart': {
            'module_name': 'chart', 
            'urlconf_additions': '%s/config/chart_urlconf_additions.py' % SCRIPT_PATH,
        },
        'panya-competition': {
            'module_name': 'competition',
            'urlconf_additions': '%s/config/competition_urlconf_additions.py' % SCRIPT_PATH,
        },
        'panya-contact': {
            'module_name': 'contact',
            'urlconf_additions': '%s/config/contact_urlconf_additions.py' % SCRIPT_PATH,
        },
        'panya-event': {
            'module_name': 'event', 
            'urlconf_additions': '%s/config/event_urlconf_additions.py' % SCRIPT_PATH,
        },
        'panya-gallery': {
            'module_name': 'gallery',
            'urlconf_additions': '%s/config/gallery_urlconf_additions.py' % SCRIPT_PATH,
        },
        'panya-music': {
            'module_name': 'music', 
            'urlconf_additions': '%s/config/music_urlconf_additions.py' % SCRIPT_PATH,
        },
        'panya-post': {
            'module_name': 'post', 
        },
        'panya-show': {
            'module_name': 'show', 
            'urlconf_additions': '%s/config/show_urlconf_additions.py' % SCRIPT_PATH,
        },
        'panya-social': {
            'module_name': 'social', 
        },
    }

class PanyaProjectTemplate(Template):
    _template_dir = 'templates/panya_project'
    summary = 'Creates a buildout providing a Django instance and Django project with selected Panya apps installed.'
    use_cheetah = True

    vars = [
        var('secret_key', 'The secret key for hashing algorithms',
            default=''.join(
                [choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
            ) for i in range(50)])),
        var('hostname', 'Hostname for the primary instance', default='localhost'),
        var('hostname_staging', 'Hostname for the staging instance', default='staging.localhost'),
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
