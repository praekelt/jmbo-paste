from setuptools import setup, find_packages

setup(
    name='panya-paste',
    version='0.0.4',
    description='Python Paste templates creating Panya buildout environments.',
    long_description = open('README.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://github.com/praekelt/panya-paste',
    packages = find_packages(),
    install_requires = [
        'setuptools',
        'PasteScript>=1.7',
    ],
    include_package_data=True,
    entry_points = """
        [paste.paster_create_template]
        panya_minimal=panya_paste.templates:PanyaMinimalTemplate
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
