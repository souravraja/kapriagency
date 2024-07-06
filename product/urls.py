
from django.urls import path,include
from . import views
urlpatterns=[
    path("company/",views.companyname,name='companyname'),
    path('productlist/',views.productitem,name='productitem'),
    path('productlistycatagory/<int:pk>',views.productitembycatagory,name='productitemcatagoty'),
    path('productlistybrannt/<int:pk>',views.productitembybrant,name='productitembybrant'),
    path('productdetails/<int:pk>',views.productdetails,name='productdetals'),
    path('catagory',views.catagory,name='catagory'),
    path('cart',views.cart,name='cart'),
    path('Addtocart',views.Addtocart,name='Addtocart'),
]
