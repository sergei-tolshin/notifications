from django.contrib import admin

from .models import Template


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'method', 'created', 'modified',)
    list_filter = ('method',)
    search_fields = ('name',)
