from setuptools import setup, find_packages

setup(
    name='panya-paste-templates',
    version='0.0.1',
    description='Python Paste templates creating Panya buildout environments.',
    long_description = open('README.rst', 'r').read(),
    author= open('AUTHORS', 'r').read(),
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://github.com/praekelt/panya-paste-templates',
    packages = find_packages(),
    install_requires = [
        'setuptools',
        'PasteScript>=1.7',
    ],
    entry_points = """
        [paste.paster_create_template]
        buildout=panya_paste_templates.templates:BuildoutTemplate
    """,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
