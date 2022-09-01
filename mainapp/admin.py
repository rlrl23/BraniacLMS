from atexit import register
from django.contrib import admin
from mainapp import models as mainapp_models

# Register your models here.


@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ['title', 'body', 'preambule']


@admin.register(mainapp_models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'num', 'title', 'deleted', 'get_course_name']
    ordering = ["-course__name", "-num"]
    list_per_page = 5
    list_filter = ['course', 'deleted', 'created']
    actions = ["mark_deleted"]

    def get_course_name(self, obj):
        return obj.course.name

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = ("Mark deleted")

    get_course_name.short_description = ("Course")
