from django.shortcuts import render, redirect
from django.utils import timezone
from .models import PasteJobURL
from .forms import JobURLForm


def job_translation(request):
    if request.method == "POST":
        form = JobURLForm(request.POST)
        if form.is_valid():
            print form.errors
            paste = form.save(commit=False)
            paste.save()
    else:
       form = JobURLForm()
    return render(request, 'translations/job_translation.html', {'form': form})
