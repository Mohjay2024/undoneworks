from django.db import models
from django.utils.text import slugify

# --- YOUR OLD MODELS (keep them) ---
class Article(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='articles/covers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.caption or f"Photo {self.id}"

class Booking(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    event_type = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.event_type}" if self.name else f"Booking {self.id}"

# --- NEW FOLDER SYSTEM FOR EVENTS (add this) ---
def event_photo_path(instance, filename):
    event_slug = slugify(instance.event.title)
    return f"events/{event_slug}/{filename}"

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class EventPhoto(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to=event_photo_path)
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.event.title} - {self.caption}"