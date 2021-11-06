from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message

# @admin.register(Room)
# class RoomAdmin(admin.ModelAdmin):
#     list_display = ('host','name', 'created', 'updated')
#     list_filter = ('host', 'topic', 'name', 'created', 'updated')
#     search_fields = ('topic', 'name')

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
