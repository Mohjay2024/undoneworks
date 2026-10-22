from django.contrib import admin
from .models import Article, Photo, Booking, Event, EventPhoto

class EventPhotoInline(admin.TabularInline):
    model = EventPhoto
    extra = 3

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    inlines = [EventPhotoInline]

admin.site.register(Article)
admin.site.register(Photo)
admin.site.register(Booking)
admin.site.register(EventPhoto)