==============
django-omakase
==============

A project template for Django 1.5.

To use this project follow these steps:

#. Create your working environment
#. Install Django
#. Create the new project using the django-omakase template
#. Install additional dependencies
#. Push to production

*note: these instructions show creation of a project called "icecream".  You
should replace this name with the actual name of your project.*

Working Environment
===================

#. Install python
#. Install pip::

    $ sudo easy_install pip

#. Install virtualenvwrapper::

    $ sudo pip install virtualenvwrapper
    $ source /usr/local/bin/virtualenvwrapper.sh

#. Create your virtualenv::

    $ mkvirtualenv icecream

#. Install Django into the virtualenv::

    $ pip install django

Creating your Project
=====================

To create a new Django project called '**icecream**' using django-omakase, run the following command::

    $ django-admin.py startproject --template=https://github.com/team-stroller/django-omakase/zipball/master --extension=py,rst,html --name=Procfile icecream

Setup Development Environment
==============================

Install the project's local dependencies::

    $ pip install -r requirements/local.txt

Install postgres. Create a DB and a superuser. The database's name, username, and password must all be the project name (icecream)::

    $ createdb icecream
    $ createuser -P
    $ python icecream/manage.py syncdb
    $ python icecream/manage.py migrate djcelery

Install foreman. Run your development server::

    $ foreman start

Setup Production on Heroku
==========================

You will need the `Heroku Toolbelt`_ installed. You can use this to create your Heroku app::

    $ heroku create

.. _Heroku Toolbelt: https://toolbelt.heroku.com/

Environment Variables
---------------------

The `DJANGO_SETTINGS_MODULE` environment variable must be set to `icecream.settings.production`. The `SECRET_KEY` environment variable must be set to a secure string::

   $ heroku config:set DJANGO_SETTINGS_MODULE=icecream.settings.production SECRET_KEY=mysupersecretkey -r heroku

Settings
--------

You need to set the `ALLOWED_HOSTS` setting in `production.py`. This should be the domain names of your production server::

   ALLOWED_HOSTS = ['eaticecream.com']

Addons
------

You need the Redis Cloud addon or the `REDISCLOUD_URL` variable set. This is used by celery::

    $ heroku addons:add rediscloud

Acknowledgements
================

    - Mad props to TwoScoops_.
    - Many thanks to Randall Degges for the inspiration to write the book and django-skel.
    - All of the contributors_ to this project.

.. _contributors: https://github.com/twoscoops/django-twoscoops-project/blob/master/CONTRIBUTORS.txt
.. _TwoScoops: https://github.com/twoscoops/django-twoscoops-project
