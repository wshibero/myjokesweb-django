from django.shortcuts import render
from pyjokes import get_joke

# Create your views here.

def index(request):
  return render(request, 'index.html', {"joke": get_joke(language="en", category="all")})
