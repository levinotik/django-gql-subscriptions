# """
# ASGI config for myapp project.
#
# It exposes the ASGI callable as a module-level variable named ``application``.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
# """
#
# from channels.routing import get_default_application
# import os
#
# from django.core.asgi import get_asgi_application
#
# # from myapp.myapp import application as myapp
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
#
# # application = myapp
# application = get_asgi_application()
