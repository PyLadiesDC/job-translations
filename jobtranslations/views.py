from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Paste
from .forms import PasteForm


def job_translation(request):
    if request.method == "POST":
        form = PasteForm(request.POST,)# instance=post)
        if form.is_valid():
            print form.errors
            paste = form.save(commit=False)
            paste.save()
            #form = PasteForm
    else:
       form = PasteForm()#instance=paste)
    return render(request, 'translations/job_translation.html', {'form': form})
