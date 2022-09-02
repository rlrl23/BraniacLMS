from atexit import register
from django.contrib import admin
from mainapp import models as mainapp_models

# Register your models here.


@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ['title', 'body', 'preambule']
    list_filter = ['created']


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


@admin.register(mainapp_models.CourseTeachers)
class CourseTeachersAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_first', 'name_second', 'deleted']
    list_filter = ['course', 'deleted']


@admin.register(mainapp_models.Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cost', 'created', 'deleted']
    list_filter = ['created']
    search_fields = ['name', 'description']
