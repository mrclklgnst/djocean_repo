from django.shortcuts import render
from .models import Ocean

def index(request):
    oceans = Ocean.objects.all()
    con = {'ocean_data': oceans}
    return render(request, "oceanapp/index.html", con)

# Create your views here.
