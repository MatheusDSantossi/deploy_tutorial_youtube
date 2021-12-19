import environ

from tutorialdjango.settings.base import *

env = environ.Env()

DEBUG = env.bool("DEBUG", False) #POR EXEMPLO SE FOR "True", True e "False", False

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    "default": env.db
}

#OLHA O SITE PRIMEIRO
