
from django.urls import path,include
from . import views
urlpatterns=[
    path("company/",views.companyname,name='companyname'),
    path('productlist/',views.productitem,name='productitem')
]
