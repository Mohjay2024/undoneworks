from django.db import models
from django.utils.text import slugify

# --- KEEP YOUR OLD MODELS ---
class Article(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(blank=True)
    content = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='articles/covers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.caption or f"Photo {self.id}"

class Booking(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    event_type = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.name} - {self.event_type}" if self.name else f"Booking {self.id}"

# --- NEW EVENT SYSTEM WITH STABLE ID FOLDERS ---
def event_photo_path(instance, filename):
    # Uses ID - so you can rename title anytime, folder stays same
    # If event not saved yet (no ID), use temp slug
    if instance.event_id:
        return f"events/{instance.event_id}/{filename}"
    else:
        slug = slugify(instance.event.title) if instance.event.title else "temp"
        return f"events/temp-{slug}/{filename}"

class Event(models.Model):
    title = models.CharField(max_length=200, help_text="You can change this anytime, folder stays same")
    date = models.DateField()
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

class EventPhoto(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to=event_photo_path)
    caption = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"Event {self.event_id} - {self.caption or self.image.name}"