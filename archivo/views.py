from django.shortcuts import render
from .models import Area

def index(request):
    areas = Area.objects.all()
    return render(request, 'archivo/index.html', {'areas': areas})