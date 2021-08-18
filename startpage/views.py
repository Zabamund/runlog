from django.shortcuts import render
from runs.models import Run

def home(request):
    """Render the homepage"""
    last_run = Run.objects.order_by('-id')[0]
    return render(request, 'startpage/home.html', {'last_run': last_run})