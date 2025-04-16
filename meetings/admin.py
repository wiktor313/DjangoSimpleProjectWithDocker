from django.contrib import admin

from meetings.models import Meeting, Room
from django.contrib.admin import ModelAdmin
#admin.site.register(Meeting)
@admin.register(Meeting)
class MeetingAdmin(ModelAdmin):
    list_display = ('id','title', 'date', 'start_time', 'room')
    search_fields = ('title',)
    list_filter = ('room',)
    ordering = ('date', 'start_time')

admin.site.register(Room)

# Register your models here.
