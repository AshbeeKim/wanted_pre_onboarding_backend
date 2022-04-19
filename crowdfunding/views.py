from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Products
import datetime

# Create your views here.
def index(request):
    return HttpResponse("Hello, Welcome to CrowdFunding.")

def product_view(request):
    products = Products.objects.all()
    return render(request, 'index.html', {'posts': products})