from django.shortcuts import render
from .models import Item,Supplier

# Create your views here.

def welcome(request):

    return render(request, 'test.html', )

