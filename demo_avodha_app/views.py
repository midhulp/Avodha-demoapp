from django.shortcuts import render,redirect
from . forms import ModeForm

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

def update(request,id):
    obj=shop.objects.get(id=id)
    form = ModeForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'obj':obj})
