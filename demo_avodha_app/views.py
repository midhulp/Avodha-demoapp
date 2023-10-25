from django.http import HttpResponse
from django.shortcuts import render

from .models import shop

# Create your views here.
def demo(request):
    obj=shop.objects.all()
    return render(request,"home.html",{'products':obj})

def detail(request,shop_id):
    product1=shop.objects.get(id=shop_id)
    return render(request,"details.html",{'prod':product1})
