from django.shortcuts import render
from django.core.cache import cache
from django.contrib.contenttypes.models import ContentType


def home(request):
   
    
    return render(request, 'base.html', {
    })


