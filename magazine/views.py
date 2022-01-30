from django.http import HttpResponseRedirect, FileResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import random

from .models import Profile, Magazine, About


def homepage(request):
    magazines = Magazine.objects.filter(featured=False)
    normal_featured = random.sample(list(magazines), 2)
    featured = Magazine.objects.filter(featured=True)
    special_featured = random.sample(list(featured), 2)

    featured_magazines = normal_featured + special_featured
    return render(request, 'index.html', {'magazines': featured_magazines, 'featured': special_featured})


def about(request):
    paragraphs = About.objects.all()
    return render(request, 'about.html', {'paragraphs': paragraphs})


def magazine_all(request):
    magazines = Magazine.objects.all()
    magazines_years = Magazine.objects.values('publish_year').distinct()
    return render(request, 'magazine_list.html', {'magazines': magazines, 'publish_years': magazines_years})


def magazine_detail(request, slug):
    magazine = get_object_or_404(Magazine, slug=slug)
    return render(request, 'magazine_detail.html', {'magazine': magazine})
