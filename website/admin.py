from django.contrib import admin
from .models import Service, Testimonial, BlogPost, ContactMessage
from django.utils.html import format_html

# Registering models so they appear in the Django Admin panel.
# This allows staff to add/edit/delete records easily.


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "icon")      # Fields shown in admin list
    search_fields = ("title",)                            # Enables search by service title


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "quote", "screenshot_preview")

    def has_text(self, obj):
        return bool(obj.quote)
    has_text.boolean = True     # Displays as ✅/❌ in admin
    has_text.short_description = "Text?"

    def screenshot_preview(self, obj):
        if obj.screenshot:
            return format_html('<img src="{}" style="max_height: 100px;">', obj.screenshot.url)
        return "No screenshot"
    screenshot_preview.short_description = "Screenshot"


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}  # Auto-fill slug from title

    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" style="max-height: 80px;">', obj.cover_image.url)
        return "No image"
    cover_preview.short_description = "Cover"


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "sent_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("sent_at",)  # Prevent editing timestamps 