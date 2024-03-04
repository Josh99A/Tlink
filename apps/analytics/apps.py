import oscar.apps.analytics.apps as apps


class AnalyticsConfig(apps.AnalyticsConfig):
    name = 'apps.analytics'


    def ready(self):
        from . import receivers
        
