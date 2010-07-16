from os import path

from paste.script import command
from paste.script.templates import Template, var
from random import choice

SCRIPT_PATH =  path.abspath(path.dirname(__file__))

APP_CONFIG = {
        'django-ckeditor': {
            'module_name': 'ckeditor',
            'urlconf_additions': '%s/config/ckeditor_urlconf_additions.py' % SCRIPT_PATH,
        },
        'django-generate': {
            'module_name': 'generate',
            'find_links': ('https://github.com/praekelt/django-generate/tarball/0.0.1#egg=django-generate',),
        },
        'django-gizmo': {
            'module_name': 'gizmo', 
            'find_links': ('https://github.com/praekelt/django-gizmo/tarball/0.0.1#egg=django-gizmo',),
        },
        'django-googlesearch': {
            'module_name': 'googlesearch',
            'find_links': ('https://github.com/praekelt/django-googlesearch/tarball/0.0.3#egg=django-googlesearch',),
            'urlconf_additions': '%s/config/googlesearch_urlconf_additions.py' % SCRIPT_PATH,
        },
        'django-likes': {
            'module_name': 'likes',
            'find_links': ('https://github.com/praekelt/django-likes/tarball/0.0.1#egg=django-likes',),
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
            'find_links': ('https://github.com/praekelt/django-profile/tarball/0.0.2#egg=django-profile',),
            'model_additions': '%s/config/profile_model_additions.py' % SCRIPT_PATH,
        },
        'django-publisher': {
            'module_name': 'publisher',
            'find_links': ('https://github.com/praekelt/django-publisher/tarball/0.0.1#egg=django-publisher',),
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
            'find_links': ('https://github.com/praekelt/django-richcomments/tarball/0.0.1#egg=django-richcomments',),
            'urlconf_additions': '%s/config/richcomments_urlconf_additions.py' % SCRIPT_PATH,
            'buildout_media_links': ('django-richcomments://richcomments/media/richcomments',),
        },
        'django-section': {
            'module_name': 'section',
        },
        'panya': {
            'module_name': 'panya',
            'find_links': ('https://github.com/praekelt/panya/tarball/0.0.5#egg=panya',),
            'urlconf_additions': '%s/config/panya_urlconf_additions.py' % SCRIPT_PATH,
        },
        'panya-banner': {
            'module_name': 'banner',
            'find_links': ('https://github.com/praekelt/panya-banner/tarball/0.0.1#egg=panya-banner',),
        },
        'panya-calendar': {
            'module_name': 'cal', 
            'find_links': ('https://github.com/praekelt/panya-calendar/tarball/0.0.1#egg=panya-calendar',),
        },
        'panya-chart': {
            'module_name': 'chart', 
            'find_links': ('https://github.com/praekelt/panya-chart/tarball/0.0.3#egg=panya-chart',),
            'urlconf_additions': '%s/config/chart_urlconf_additions.py' % SCRIPT_PATH,
        },
        'panya-competition': {
            'module_name': 'competition',
            'find_links': ('https://github.com/praekelt/panya-competition/tarball/0.0.3#egg=panya-competition',),
            'urlconf_additions': '%s/config/competition_urlconf_additions.py' % SCRIPT_PATH,
        },
        'panya-contact': {
            'module_name': 'contact',
            'find_links': ('https://github.com/praekelt/panya-contact/tarball/0.0.4#egg=panya-contact',),
            'urlconf_additions': '%s/config/contact_urlconf_additions.py' % SCRIPT_PATH,
        },
        'panya-event': {
            'module_name': 'event', 
            'find_links': ('https://github.com/praekelt/panya-event/tarball/0.0.3#egg=panya-event',),
            'urlconf_additions': '%s/config/event_urlconf_additions.py' % SCRIPT_PATH,
        },
        'panya-gallery': {
            'module_name': 'gallery',
            'find_links': ('https://github.com/praekelt/panya-gallery/tarball/0.0.1#egg=panya-gallery',),
            'urlconf_additions': '%s/config/gallery_urlconf_additions.py' % SCRIPT_PATH,
        },
        'panya-music': {
            'module_name': 'music', 
            'find_links': ('https://github.com/praekelt/panya-music/tarball/0.0.3#egg=panya-music',),
            'urlconf_additions': '%s/config/music_urlconf_additions.py' % SCRIPT_PATH,
        },
        'panya-post': {
            'module_name': 'post', 
            'find_links': ('https://github.com/praekelt/panya-post/tarball/0.0.1#egg=panya-post',),
        },
        'panya-show': {
            'module_name': 'show', 
            'find_links': ('https://github.com/praekelt/panya-show/tarball/0.0.5#egg=panya-show',),
            'urlconf_additions': '%s/config/show_urlconf_additions.py' % SCRIPT_PATH,
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
