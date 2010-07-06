from os import path

from paste.script import command
from paste.script.templates import Template, var
from random import choice

SCRIPT_PATH =  path.abspath(path.dirname(__file__))

APP_CONFIG = {
        'django-ckeditor': {
            'module_name': 'ckeditor',
        },
        'django-generate': {
            'module_name': 'generate',
            'find_links': ('https://github.com/praekelt/django-generate/tarball/master#egg=django-generate',),
        },
        'django-gizmo': {
            'module_name': 'gizmo', 
            'find_links': ('https://github.com/praekelt/django-gizmo/tarball/master#egg=django-gizmo',),
        },
        'django-googlesearch': {
            'module_name': 'googlesearch',
            'find_links': (
                'https://github.com/praekelt/django-googlesearch/tarball/master#egg=django-googlesearch',
                'https://github.com/downloads/praekelt/eggs/django_googlesearch-0.0.2-py2.6.egg#egg=django-googlesearch',
            ),
        },
        'django-likes': {
            'module_name': 'likes',
            'find_links': ('https://github.com/praekelt/django-likes/tarball/master#egg=django-likes',),
        },
        'django-preferences': {
            'module_name': 'preferences'
        },
        'django-profile': { 
            'module_name': 'profile', 
            'find_links': ('https://github.com/praekelt/django-profile/tarball/master#egg=django-profile',),
            'model_additions': '%s/config/profile_model_additions.py' % SCRIPT_PATH,
        },
        'django-publisher': {
            'module_name': 'publisher',
            'find_links': (
                'https://github.com/praekelt/django-publisher/tarball/master#egg=django-publisher',
                'https://github.com/downloads/praekelt/eggs/django_publisher-0.0.1-py2.6.egg#egg=django-publisher',
            ),
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
            'find_links': ('https://github.com/praekelt/django-richcomments/tarball/master#egg=django-richcomments',),
        },
        'django-section': {
            'module_name': 'section',
        },
        'panya': {
            'module_name': 'panya',
            'find_links': ('https://github.com/praekelt/panya/tarball/master#egg=panya',),
            'urlconf_additions': '%s/config/panya_urlconf_additions.py' % SCRIPT_PATH,
        },
        'panya-banner': {
            'module_name': 'banner',
            'find_links': (
                'https://github.com/praekelt/panya-banner/tarball/master#egg=panya-banner',
                'https://github.com/downloads/praekelt/eggs/panya_banner-0.0.1-py2.6.egg#egg=panya-banner',
            ),
        },
        'panya-calendar': {
            'module_name': 'cal', 
            'find_links': (
                'https://github.com/praekelt/panya-calendar/tarball/master#egg=panya-calendar',
                'https://github.com/downloads/praekelt/eggs/panya_calendar-0.0.1-py2.6.egg#egg=panya-calendar',
            ),
        },
        'panya-chart': {
            'module_name': 'chart', 
            'find_links': ('https://github.com/praekelt/panya-chart/tarball/0.0.1#egg=panya-chart',),
        },
        'panya-competition': {
            'module_name': 'competition',
            'find_links': ('https://github.com/praekelt/panya-competition/tarball/master#egg=panya-competition',),
        },
        'panya-contact': {
            'module_name': 'contact',
            'find_links': ('https://github.com/praekelt/panya-contact/tarball/master#egg=panya-contact',),
        },
        'panya-event': {
            'module_name': 'event', 
            'find_links': ('https://github.com/praekelt/panya-event/tarball/master#egg=panya-event',),
        },
        'panya-gallery': {
            'module_name': 'gallery',
            'find_links': ('https://github.com/praekelt/panya-gallery/tarball/master#egg=panya-gallery',),
        },
        'panya-music': {
            'module_name': 'panya-music', 
            'find_links': ('https://github.com/praekelt/panya-music/tarball/master#egg=panya-music',),
        },
        'panya-post': {
            'module_name': 'post', 
            'find_links': ('https://github.com/praekelt/panya-post/tarball/master#egg=panya-post',),
        },
        'panya-show': {
            'module_name': 'show', 
            'find_links': ('https://github.com/praekelt/panya-show/tarball/master#egg=panya-show',),
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
    ]

    def pre(self, command, output_dir, vars):
        vars['app_config'] = APP_CONFIG
        app_keys = APP_CONFIG.keys()
        app_keys.sort()
        for key in app_keys:
            vars[key]=command.challenge('Install %s?: y/n' % key, 'y', True)
