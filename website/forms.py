from django import forms

class ContactForm(forms.Form):
    """
    Contact form used on the website
    """
    name = forms.CharField(
        max_length=100,
        label="Full Name",
        widget=forms.TextInput(attrs={
            "placeholder": "Your full name",
            "class": "w-full px-4 py-3 rounded-lg border focus:outline-none focus:ring-2 focus:ring-blue-500"
        })
    )

    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={
            "placeholder": "you@example.com",
            "class": "w-full px-4 py-3 rounded-lg border focus:outline-none focus:ring-2 focus:ring-blue-500"
        })
    )

    message = forms.CharField(
        label="Message",
        widget=forms.TextInput(attrs={
            "rows": 5,
            "placeholder": "Tell us how we can help you...",
            "class": "w-full px-4 py-3 rounded-lg border focus:outline-none focus:ring-2 focus:ring-blue-500"
        })
    )