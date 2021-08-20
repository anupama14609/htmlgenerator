from django.shortcuts import render
from .forms import HtmlGeneratorForm
from .models import HtmlGenerator

def home(request):
    form = HtmlGeneratorForm()
    return render(request, 'app/home.html',{'form':form})

