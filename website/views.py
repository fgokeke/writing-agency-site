from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Service, Testimonial, BlogPost, ContactMessage
from .forms import ContactForm
# Create your views here.

def home(request):
    # Renders the homepage template, which extends base.html
    return render(request, 'home.html')

def services(request):
    """
    Fetches all services from the database
    and sends them to the service template.
    """
    services = Service.objects.all()
    return render(request, "services.html", {
        "services": services
    })


def testimonials(request):
    """
    Fetches all testimonials and sends them to the template.
    """
    testimonials = Testimonial.objects.all()
    return render(request, "testimonials.html", {
        "testimonials": testimonials
    })

def about(request):
    """
    Renders the About page.
    This page explains who the agency is, what we do,
    and optionally introduces the team.
    """
    return render(request, "about.html")

def blog_list(request):
    """
    Displays a list of all blog posts.
    """
    posts = BlogPost.objects.all()
    return render(request, "blog_list.html", {
        "posts": posts
    })


def blog_detail(request, slug):
    """
    Displays a single blog post.
    """
    post = BlogPost.objects.get(slug=slug)
    return render(request, "blog_detail.html", {
        "post": post
    })

def contact(request):
    """
    Displays and processes the contact form.
    """
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            # Save message to database
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )

            # Send email (console in dev)

            send_mail(
                subject=f"New Contact Message from {name}",
                message=(
                    f"Name: {name}\n"
                    f"Email: {email}\n\n"
                    f"Message:\n{message}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["your-email@example.com"],
            )

            # User feedback
            messages.success(
                request,
                "Thank you for reaching out. We’ll get back to you shortly."
            )

            return redirect("contact")

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})