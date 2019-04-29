from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from api import models

# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    """
    Extend the base Django UserAdmin with support
    """

    date_hierarchy = 'date_joined'
    ordering = ['-date_joined']
    list_display = list(DjangoUserAdmin.list_display) + ['date_joined']


@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    """
    Extend the base Django UserAdmin with support
    """

    ordering = ['-name']


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    """
    Extend the base Django UserAdmin with support
    """

    ordering = ['-title']
