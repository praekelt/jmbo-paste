from setuptools import setup, find_packages

setup(
    name='panya-paste',
    version='0.1.0',
    description='Python Paste templates creating Panya buildout environments.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://github.com/praekelt/panya-paste',
    packages = find_packages(),
    install_requires = [
        'Cheetah>=2.4.2.1',
        'PasteScript',
        'setuptools',
    ],
    include_package_data=True,
    entry_points = """
        [paste.paster_create_template]
        panya_project=panya_paste.templates:PanyaProjectTemplate
    """,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Paste",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False
)
