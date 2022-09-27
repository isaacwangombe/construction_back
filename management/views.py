from django.shortcuts import render
from .models import Item,Supplier, Units, Date

# Create your views here.

def welcome(request):
    dates = Date.get_all()

    return render(request, 'test.html', {"dates":dates} )

