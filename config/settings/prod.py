from .base import *

DEBUG = False

ALLOWED_HOSTS = ['sm-newsletter.herokuapp.com', ]


import django_heroku

django_heroku.settings(locals())

