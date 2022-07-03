from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import (App, Event, Newsletter, Notice, Template, UserNotice,
                     UserTime)


class EventInline(admin.TabularInline):
    model = Event
    extra = 1
    fields = ('title', 'name',)


class NoticeInline(admin.TabularInline):
    model = Notice
    extra = 1


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    inlines = (EventInline,)
    list_display = ('title', 'name', 'created',)
    search_fields = ('title', 'name',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = (NoticeInline,)
    list_display = ('title', 'name', 'created',)
    list_filter = ('app',)
    search_fields = ('title', 'name',)


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'task_name', 'by_default', 'created', 'modified',)
    list_filter = ('notice__method', 'notice__event__app',
                   'notice__event__title',)
    search_fields = ('name',)

    @admin.display(description=_('task name'))
    def task_name(self, obj):
        return '{event}.{method}'.format(event=obj.notice.event,
                                         method=obj.notice.method)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('title', 'clocked_time', 'created', 'enabled')
    list_filter = ('clocked_time',)
    search_fields = ('title',)
    exclude = ('task',)


@admin.register(UserNotice)
class UserNoticeAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'event', 'method', 'created',)
    list_filter = ('notice__method', 'notice',)

    @admin.display(description=_('event'))
    def event(self, obj):
        return obj.notice.event.title

    @admin.display(description=_('method'))
    def method(self, obj):
        return obj.notice.get_method_display()


@admin.register(UserTime)
class UserTimeAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'timezone', 'time_from', 'time_to')
    list_filter = ('timezone',)
