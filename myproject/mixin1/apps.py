from django.apps import AppConfig


class Mixin1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mixin1'
