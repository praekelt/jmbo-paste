from paste.script import command
from paste.script.templates import Template, var
from random import choice

APP_CHOICES = (
    ('ckeditor','django-ckeditor'),
    ('generate', 'django-generate', ('https://github.com/praekelt/django-generate/tarball/master#egg=django-generate',)),
    ('gizmo', 'django-gizmo', ('https://github.com/praekelt/django-gizmo/tarball/master#egg=django-gizmo',)),
    ('googlesearch', 'django-googlesearch', ('https://github.com/praekelt/django-googlesearch/tarball/master#egg=django-googlesearch',)),
    ('likes', 'django-likes', ('https://github.com/praekelt/django-likes/tarball/master#egg=django-likes',)),
    ('pagemenu', 'django-pagemenu', ('https://github.com/praekelt/django-pagemenu/tarball/master#egg=django-pagemenu',)),
    ('preferences', 'django-preferences'),
    ('profile', 'django-profile', ('https://github.com/praekelt/django-profile/tarball/master#egg=django-profile',)),
    ('publisher', 'django-publisher', (
        'https://github.com/praekelt/django-publisher/tarball/master#egg=django-publisher',
        'https://github.com/downloads/praekelt/eggs/django_publisher-0.0.1-py2.6.egg#egg=django-publisher',
        )
    ),
    ('recaptcha', 'django-recaptcha',),
    ('registration', 'django-registration'),
    ('richcomments', 'django-richcomments', ('https://github.com/praekelt/django-richcomments/tarball/master#egg=django-richcomments',)),
    ('section', 'django-section'),
    ('banner', 'panya-banner', (
        'https://github.com/praekelt/panya-banner/tarball/master#egg=panya-banner',
        'https://github.com/downloads/praekelt/eggs/panya_banner-0.0.1-py2.6.egg#egg=panya-banner',
        )
    ),
    ('calendar', 'panya-calendar', ('https://github.com/praekelt/panya-calendar/tarball/master#egg=panya-calendar',)),
    ('chart', 'panya-chart', (
        'https://github.com/praekelt/panya-chart/tarball/master#egg=panya-chart',
        'https://github.com/downloads/praekelt/eggs/panya_chart-0.0.1-py2.6.egg#egg=panya-chart',
        )
    ),
    ('competition', 'panya-competition', ('https://github.com/praekelt/panya-competition/tarball/master#egg=panya-competition',)),
    ('contact', 'panya-contact', ('https://github.com/praekelt/panya-contact/tarball/master#egg=panya-contact',)),
    ('event', 'panya-event', ('https://github.com/praekelt/panya-event/tarball/master#egg=panya-event',)),
    ('gallery', 'panya-gallery', ('https://github.com/praekelt/panya-gallery/tarball/master#egg=panya-gallery',)),
    ('music', 'panya-music', ('https://github.com/praekelt/panya-music/tarball/master#egg=panya-music',)),
    ('post', 'panya-post', ('https://github.com/praekelt/panya-post/tarball/master#egg=panya-post',)),
    ('show', 'panya-show', ('https://github.com/praekelt/panya-show/tarball/master#egg=panya-show',)),
)

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
        vars['app_choices'] = APP_CHOICES
        for choice in APP_CHOICES:
            vars[choice[0]]=command.challenge('Install %s?: y/n' % choice[1], 'y', True)
