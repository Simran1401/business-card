from django.apps import AppConfig


class CardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Cards'

    def ready(self):
        from . import scheduler
        scheduler.start()

