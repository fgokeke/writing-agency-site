# website/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import BlogPost  # <-- your BlogPost model

# ---- Sitemap for static pages ----
class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        # Use the URL names defined in website/urls.py
        return ['home', 'about', 'services', 'contact', 'testimonials', 'blog_list']

    def location(self, item):
        return reverse(item)


# ---- Sitemap for blog posts ----
class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return BlogPost.objects.all()  # all blog posts

    def lastmod(self, obj):
        return obj.created_at  # using created_at since you don’t have updated_at