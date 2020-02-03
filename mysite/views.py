from django.shortcuts import render
from mysite.models import Page

def index(request):
    page = Page.objects.get(alias='index')
    return render(request,"mysite/index.html",{"page": page})