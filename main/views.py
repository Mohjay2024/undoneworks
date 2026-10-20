from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import Booking, Article, Photo

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def principles(request):
    return render(request, 'main/principles.html')

def services(request):
    return render(request, 'main/services.html')

def contact(request):
    success = False
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email_val = request.POST.get('email')
        service = request.POST.get('service')
        message = request.POST.get('message')

        Booking.objects.create(
            name=name,
            phone=phone,
            email=email_val,
            service=service,
            message=message
        )

        full_message = f"""
New Booking from Arya Samaj Website
Name: {name}
Phone: {phone}
Email: {email_val}
Service: {service}
Message: {message}
"""
        send_mail(
            subject=f"New {service} Booking - {name}",
            message=full_message,
            from_email='arya.samaj.nairobi@gmail.com',
            recipient_list=['arya.samaj.nairobi@gmail.com'],
            fail_silently=False,
        )
        success = True

    return render(request, 'main/contact.html', {'success': success})

def articles(request):
    posts = Article.objects.filter(is_published=True)
    all_photos = Photo.objects.all().order_by('-uploaded_at')
    return render(request, 'main/articles.html', {'posts': posts, 'all_photos': all_photos})

def article_detail(request, slug):
    post = get_object_or_404(Article, slug=slug)
    return render(request, 'main/article_detail.html', {'post': post})