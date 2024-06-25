from django.shortcuts import render
from .models import OurWorkingCompany
# Create your views here.


def companyname(request):
    ourWorkingCompany=OurWorkingCompany.objects.all()
    return render(request,'productlist/companyname/name.html',{'company':ourWorkingCompany})


def home(request):
    return render(request,'productlist/home/home.html')