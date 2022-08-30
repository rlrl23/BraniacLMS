from atexit import register
from django.contrib import admin
from mainapp import models as mainapp_models

# Register your models here.


@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
    pass
