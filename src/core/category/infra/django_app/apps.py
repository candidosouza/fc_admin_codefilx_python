from typing import Any, Optional
from django.apps import AppConfig, apps


class CategoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.category.infra.django_app'
    verbose_name = 'Categorias'
    label = 'category'

    def ready(self):
        import core.category.infra.django_app.models
        # category_model = apps.get_model('core.category.infra.django_app', 'CategoryModel')
        # print(category_model.objects.count())
