from django.apps import AppConfig


class DispatchConfig(AppConfig):
    name = 'dispatch'

    def ready(self):
        import dispatch.signals
