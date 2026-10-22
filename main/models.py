import os
from django.utils.text import slugify

def event_photo_path(instance, filename):
    # instance is the photo, instance.event is the event
    event_slug = slugify(instance.event.title)  # diwali-2024
    return f"events/{event_slug}/{filename}"

class Event(models.Model):
    title = models.CharField(max_length=200)  # e.g. Diwali 2024
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title

class EventPhoto(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to=event_photo_path)
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.event.title} - {self.caption}"