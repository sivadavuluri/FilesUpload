from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.

def Index(request):
    return render(request, 'profiles/index.html')

def Upload_Profile(request):
    r = None
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            r = form.save()
    else:
        form = ProfileForm()
    return render(request, 'profiles/profile.html', {'form': form, 'obj': r})

def Search_Profile(request):
    row = None
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            pid = form.cleaned_data['profile_id']
            row = profiles.objects.get(id=pid)
    else:
        form = SearchForm()
    return render(request, 'profiles/search.html', {'form': form, 'row': row})