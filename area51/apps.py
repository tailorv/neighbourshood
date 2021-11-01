from django.apps import AppConfig

class HoodappConfig(AppConfig):
    name = 'area51'

    def ready(self):
        import area51.signals