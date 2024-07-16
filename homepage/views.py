from django.shortcuts import render
from product.models import Product,productCatagory
# Create your views here.
def home(request):
    products=Product.objects.all()
    catagory= productCatagory.objects.order_by('?')[:6]
    for i in catagory:
        print(i.name)
        print(i.img)
    context={
        'product': products,
        'catagor':catagory

    }
    return render(request,'homepage/home.html',context)