Jmbo Paste
==========
Python Paste templates creating Jmbo Buildout environments.

This packages is part of the larger `Jmbo <http://www.jmbo.org>`_ project .

.. contents:: Contents
    :depth: 2

jmbo-paste simplifies the process of creating a Jmbo development environment.

Dependencies
------------

Jmbo requires `Python <http://www.python.org>`_, the Python development library as well as `Python Setuptools <http://pypi.python.org/pypi/setuptools>`_. These can be installed as follows::

    $ sudo apt-get install python python-dev python-setuptools

jmbo-paste utilizes `Python Paste <http://pythonpaste.org/>`_ to create project boilerplate and structure for you, which you can install as follows::
    
    $ easy_install paste

Creating a project
------------------

Once all dependencies have been installed you can create your project layout. From the commandline ``cd`` into a directory where you'd like to store your project then run the following command::

    $ paster create -t jmbo_project

Follow the prompts to configure your project. For the purposes of this example please provide a project name of ``mysite`` and answer ``yes`` to all installation prompts. This will create a ``mysite`` directory containing your new project's code with directory structure as follows::
    
    mysite/
        bootstrap.py
        buildout.cfg
        buildout_templates/
            nginx.conf
            supervisor.uwsgi
        log/
        media/
            uploads/
        production.cfg
        qa.cfg
        src/
            mysite/
                MANIFEST.in
                mysite/
                    dev_settings.py
                    gizmos.py
                    __init__.py
                    media/
                        mysite/
                    models.py
                    qa_settings.py
                    settings.py
                    staging_settings.py
                    templates/
                        base.html
                    urls.py
                README.rst
                setup.py
        staging.cfg

That's quite a lot of stuff, here's a description of each file:
``bootstrap.py``: The `Buildout <http://pypi.python.org/pypi/zc.buildout>`_ file used to initially boostrap the Buildout environment. (You won't ever have to change this file so you can safely ignore it.)

``buildout.cfg``: The base Buildout configuration used by default and extended by other configurations. If you're unfamiliar with Buildout I suggest you have a look at Jacob Kaplan-Moss' excellent `primer <http://jacobian.org/writing/django-apps-with-buildout/>`_.

``buildout_templates/nginx.conf``: Template file used by Buildout to create a `Nginx <http://wiki.nginx.org/>`_ configrations for your project. You should never have to edit this by hand, rather update ``buildout.cfg`` for your specific customizations.

``buildout_templates/supervisor.uwsgi``: Template file used by Buildout to create a `Supervisor <http://supervisord.org/>`_ control configuration for `uWSGI <http://projects.unbit.it/uwsgi/>`_. You should never have to edit this by hand, rather update ``buildout.cfg`` for your specific customizations.

``log/``: Empty path in which various Nginx and uWSGI logs will be stored.

``media/``: Media path from which all static content is served. During buildout various paths like the Django admin static media path and your project specific media path is symlinked here.

``media/uploads/``: Media path in which CKEditor uploads will be stored.

``production.cfg``: The production Buildout configuration extended from ``buildout.cfg`` used to create a production environment.

``qa.cfg``: The qa Buildout configuration extended from ``buildout.cfg`` used to create a quality assurance environment.

``src/``: Source path in which all your project specific code is stored.

``src/mysite/``: Root project package path, used to store packaging code.

``src/mysite/MANIFEST``: Python egg package manifest, which specifies which files to include/exclude when packaging for distribution. In most instances you can savely ignore this file.

``src/mysite/mysite/``: Project module path. All project specific module code is stored here.

``src/mysite/mysite/dev_settings.py``: Django project settings used for the default development environment. Extended from ``src/mysite/mysite/settings.py``.

``src/mysite/mysite/gizmos.py``: `django-gizmo <http://pypi.python.org/pypi/django-gizmo>`_ declarations for your project.

``src/mysite/mysite/__init__.py``: Empty file indicating that the directory is a Python package.

``src/mysite/mysite/media/``: Root project media path.

``src/mysite/mysite/media/mysite``: Media path in which all your project specific static media should be stored.

``src/mysite/mysite/models.py``: `Django ORM model <https://docs.djangoproject.com/en/dev/topics/db/models/>`_ declarations for your project.

``src/mysite/mysite/qa_settings.py``: Django project settings used for a quality assurance environment. Extended from ``src/mysite/mysite/settings.py``.

``src/mysite/mysite/settings.py``: Base Django project settings used for a production environment.

``src/mysite/mysite/staging_settings.py``: Django project settings used for a staging environment. Extended from ``src/mysite/mysite/settings.py``.

``src/mysite/mysite/templates/``: Root project templates path.

``src/mysite/mysite/templates/base.html``: Base template from which all other templates extend. See `Django's docs on templating <https://docs.djangoproject.com/en/dev/topics/templates/>`_ for more info.

``src/mysite/mysite/urls.py``: URL declarations for your project. See `Django's docs on the URL dispatcher <https://docs.djangoproject.com/en/dev/topics/http/urls/>`_ for more info.

``src/mysite/README.rst``: Readme doc in which you can document your project. Included when packaging for distribution. In most instances you can savely ignore this file.

``staging.cfg``: The staging Buildout configuration extended from ``buildout.cfg`` used to create a staging environment.

This might seem rather complicated but the only directory you really need to concern yourself with is ``src/mysite/mysite`` which follows the normal Django project layout. The rest of the files are used to create a sandboxed Buildout environment and to assist when you want to eventually deploy your project. You can treat them as boilerplate and safely ignore them for the most part.

Running a Buildout
------------------

Once your project structure has been created it's time to run a buildout. `Buildout <http://pypi.python.org/pypi/zc.buildout>`_ creates a sandboxed environment containing all the various packages required by your project.

To run a buildout you first have to bootstrap it. Bootstrapping involves downloading various files required by Buildout to, well, buildout. You only have to perform a bootstrap once on initial project setup after which Buildout's requirements will be met. Bootstrap as follows::

    $ cd mysite
    $ python bootstrap.py

When the bootstrap completes you can proceed with the actual buildout as follows::
    
    $./bin/buildout

Sit back and relax while Buildout downloads all the various packages required by your project and creates a development environment.
Buildout will create a ``bin/django`` script which is exactly the same as Django's normal `manage.py` script, except that it is configured to use the packages in your sandboxed environment.


Running the development server
------------------------------

Once the Buildout completes you are ready to run the default Jmbo application.

As always with Django though you first need to create your database with the ``sycndb`` command::
    
    $ ./bin/django syncdb

After which you can finally start the development server as follows:: 

    $ ./bin/django runserver

Now that the server's running visit `http://localhost:8000 <http://localhost:8000>`_ using your Web browser. You'll see the generic Jmbo application homepage!

And that's it, you've just created a Jmbo development environment. 
