from django.apps import AppConfig
from django.conf import settings


class SosyalMedyaAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sosyal_medya_app'

    def ready(self):
        from django.contrib.auth.models import Group
        from django.db.models.signals import post_save

        def kullaniciyi_ekle( sender, **kwargs):
            kullanici = kwargs['instance']
            if kwargs['created']:
                group, ok = Group.objects.get_or_create(name='kullanici')
                group.user_set.add(kullanici)
        
        post_save.connect( kullaniciyi_ekle, sender = settings.AUTH_USER_MODEL )
