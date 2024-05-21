from django.contrib import admin
from .models import Product,cart
# Register your models here.
@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    list_display=['id','title','mrp','our_price','product_orgin','Product_type']


@admin.register(cart)
class cart(admin.ModelAdmin):
    list_display=['id','user','Product','quantity']