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

def add_product(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        price=request.POST.get('price')
        s=shop(name=name,desc=desc,price=price)
        s.save()
        print('prooduct_added')

    return render(request,"add_product.html")
