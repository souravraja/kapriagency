from django.shortcuts import render
from .models import OurWorkingCompany,Product,productCatagory,cart
from homepage.models import Coustomer
from django.contrib.auth.models import User


# Create your views here.


def catagory(request):
    ourWorkingCompany=productCatagory.objects.all()
    return render(request,'productlist/companyname/catagory.html',{'company':ourWorkingCompany})

def companyname(request):
    ourWorkingCompany=OurWorkingCompany.objects.all()
    return render(request,'productlist/companyname/name.html',{'company':ourWorkingCompany})

def productitem(request):
    products=Product.objects.all()
    catagory= productCatagory.objects.all()

    print('catagory ',catagory)

    context={
        'product': products,
        'catagor':catagory
    }
    return render(request,'productlist/home/productlist.html',context)


def productitembycatagory(request,pk):
    productcatagory=productCatagory.objects.get(pk=pk)
    print(productcatagory.name)
    catagory=Product.objects.filter(product_catagory=productcatagory.id)
 
    context={
        'product': catagory
    }
    return render(request,'productlist/home/productlist.html',context)



def productitembybrant(request,pk):

    productorgin=OurWorkingCompany.objects.get(pk=pk)
    print(productorgin.companyName)
    catagory=Product.objects.filter(product_orgin=productorgin.id)

    context={
        'product': catagory
    }
    return render(request,'productlist/home/productlist.html',context)




def productdetails(request,pk):
    product=Product.objects.get(pk=pk)
    return render(request,'productlist/home/productdetails.html',{'product':product})


def cart(request):
    print('raja11')
    return render(request,'productlist/home/cart.html')


def Addtocart(request):
    user=request.user
    print(user)
    product_id=request.GET.get('prod_id')
    pro=Product.objects.get(id=product_id)
    Cart=cart.objects
    # cart(user==user,Product=pro).save()
    print(product_id)
    
    return render(request,'productlist/home/cart.html')