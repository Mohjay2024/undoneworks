from django.db import models
from django.utils import timezone

class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    service = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service} - {self.phone}"

    class Meta:
        ordering = ['-created_at']

# NEW - For content posting, articles and photos
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="e.g. diwali-havan-2025")
    excerpt = models.CharField(max_length=300, blank=True, help_text="Short summary shown on listing")
    content = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True, help_text="Main cover photo")
    created_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']

class Photo(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='gallery/')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True, related_name='photos', help_text="Optional - link to article")
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title or f"Photo {self.id}"

    class Meta:
        ordering = ['-uploaded_at']