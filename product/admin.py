from django.contrib import admin
from .models import Product,cart,OurWorkingCompany,productCatagory,OrderPlaced
# Register your models here.
@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    list_display=['id','title','mrp','our_price','product_orgin']
 

@admin.register(cart)
class cart(admin.ModelAdmin):
    list_display=['id','user','Product','quantity']
    
@admin.register(OurWorkingCompany)
class ourworkingcompanyAdmin(admin.ModelAdmin):
    list_display=['id','companyName']
    
@admin.register(productCatagory)
class ourworkingcompanyAdmin(admin.ModelAdmin):
    list_display=['id','name']


@admin.register(OrderPlaced)
class orderplacedyAdmin(admin.ModelAdmin):
    list_display=['id','user','customar','product','quantity','ordered_date','status']