from django.shortcuts import render

# Create your views here.

def home(request):
    # Renders the homepage template
    return render(request, 'base.html')