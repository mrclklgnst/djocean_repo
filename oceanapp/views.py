from django.shortcuts import render
from .models import Ocean, Fish

def index(request):
    oceans = Ocean.objects.all()
    fish = Fish.objects.all()
    con = {'ocean_data': oceans,
           'fish_data': fish}
    return render(request, "oceanapp/index.html", con)

# Create your views here.
