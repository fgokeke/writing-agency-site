from django.db import models
from django.utils.text import slugify


class Service(models.Model):
    """
    Represents a service offered by the writing agency.
    Example: Copywriting, Editing, Academic Writing, 
    Ghostwriting, Career Acceleration, etc.
    """
    title = models.CharField(max_length=100) # Short title of the service
    description = models.TextField()         # Detailed explanation of the service
    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Optional: store an icon class (e.g., FontAwesome) or an image URL."
    )

    def __str__(self):
        # This controls how the object displays in Django Admin & Shell
        return self.title

class Testimonial(models.Model):
    """
    Stores client testimonials. Can be plain text, 
    a screenshot (WhatsApp/email), or both.
    """
    name = models.CharField(max_length=100) # Client's name
    role = models.CharField(
        max_length=100, 
        blank=True,
        help_text="Client's role or company (optional)."
        )
    quote = models.TextField(blank=True, null=True) # Optional Text
    screenshot = models.ImageField(
        upload_to="testimonials/",
        blank=True,
        null=True,
        help_text="Upload a testimonial screenshot" 
    )

    def __str__(self):
        return f"{self.name} - {self.role}" if self.role else self.name


class BlogPost(models.Model):
    """
    Blog post for content marketing and SEO
    """
    title = models.CharField(max_length=200) # Blog post title
    slug = models.SlugField(
        unique=True,
        help_text="Unique slug for SEO-friendly URLS (e.g. 'how-to-write-a-CV')."
    )
    content = models.TextField()     # Full blog post content
    cover_image = models.ImageField(
        upload_to="blog_covers/",
        blank=True,
        null=True,
        help_text="Optional cover image for the blog post."
    )
    created_at = models.DateTimeField(auto_now_add=True)    # Auto set on creation


    def save(self, *args, **kwargs):
        # Automatically generate slug if empty
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    

    def __str__(self):
        return self.title

    

class ContactMessage(models.Model):
    """
    Stores messages submitted via the contact form.
    """
    name = models.CharField(max_length=100)     # Sender's name
    email = models.EmailField()                 # Sender's email
    message = models.TextField()                # Message content
    sent_at = models.DateTimeField(auto_now_add=True)   # Timestamp when the message was sent


    def __str__(self):
        return f'Message from {self.name} <{self.email}>'