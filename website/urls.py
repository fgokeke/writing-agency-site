from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemaps import StaticViewSitemap, BlogPostSitemap  # import your sitemap classes


sitemaps = {
    'static': StaticViewSitemap,
    'posts': BlogPostSitemap,
}

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('about/', views.about, name='about'),

    # Blog URLs
    path("blog/", views.blog_list, name="blog_list"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),

    path("contact/", views.contact, name="contact"),

     # Sitemap URL
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django-sitemap'),
]