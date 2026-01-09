from django.shortcuts import render
from .models import Service, Testimonial, BlogPost
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
    form = ContactForm()

    return render(request, "contact.html", {
        "form": form
    })