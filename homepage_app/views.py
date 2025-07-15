from django.shortcuts import render
from .models import Yozuvchilar

def homepage_view(request):
    writers = Yozuvchilar.objects.all()
    return render(request, 'home.html', {'writers': writers})
