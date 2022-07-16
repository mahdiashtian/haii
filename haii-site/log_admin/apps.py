from django.apps import AppConfig


class LogAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'log_admin'

    def ready(self):
        import log_admin.signals