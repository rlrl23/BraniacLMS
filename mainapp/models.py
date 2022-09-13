from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=256, verbose_name='Title')
    preambule = models.CharField(max_length=1024, verbose_name='Preambule')
    body = models.TextField(blank=True, null=True, verbose_name='Body')
    body_as_markdown = models.BooleanField(
        default=False, verbose_name='As markdown'
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Created', editable=False
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Edited', editable=False
    )
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.pk} {self.title}'

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta():
        verbose_name = ("News")
        verbose_name_plural = ("News")
        ordering = ('-created',)


class Courses(models.Model):
    name = models.CharField(max_length=256, verbose_name='Name')
    description = models.TextField(
        verbose_name='Description', blank=True, null=True)
    description_as_markdown = models.BooleanField(
        verbose_name='As markdown', default=False)
    cost = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='Cost', default=0)
    cover = models.CharField(
        max_length=25, default='no_image.svg', verbose_name='Cover')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Edited')
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.pk} {self.name}'

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta():
        verbose_name = ("Course")
        verbose_name_plural = ("Courses")


class CourseFeedback(models.Model):
    RATING = ((5, "⭐⭐⭐⭐⭐"), (4, "⭐⭐⭐⭐"), (3, "⭐⭐⭐"), (2, "⭐⭐"), (1, "⭐"))
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE, verbose_name=("Course"))
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, verbose_name=_("User"))
    feedback = models.TextField(
        default=("No feedback"), verbose_name=_("Feedback"))
    rating = models.SmallIntegerField(
        choices=RATING, default=5, verbose_name=_("Rating"))
    created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created"))
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course} ({self.user})"


class Lesson(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    num = models.PositiveIntegerField(verbose_name='Lesson_number')
    title = models.CharField(max_length=256, verbose_name='Name')
    description = models.TextField(
        verbose_name='Description', blank=True, null=True)
    description_as_markdown = models.BooleanField(
        verbose_name='As markdown', default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Edited')
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.pk} {self.title}'

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta:
        ordering = ('course', 'num')


class CourseTeachers(models.Model):
    course = models.ManyToManyField(Courses)
    name_first = models.CharField(max_length=128, verbose_name='Name')
    name_second = models.CharField(max_length=128, verbose_name='Surname')
    day_birth = models.DateField(verbose_name='Birh date')
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return '{0:0>3}{1}{2}'.format(self.pk, self.name_second, self.name_first)

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta():
        verbose_name = ("Teacher")
        verbose_name_plural = ("Teachers")
