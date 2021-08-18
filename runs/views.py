from django.shortcuts import render, get_object_or_404
from .models import Run

def all_runs(request):
    all_runs = Run.objects.all()
    return render(request, 'runs/all_runs.html', {'all_runs': all_runs})

def detail(request, run_id):
    run = get_object_or_404(Run, pk=run_id)
    return render(request, 'runs/detail.html', {'id': run_id, 'run': run})