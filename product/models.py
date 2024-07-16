from django.db import models
from homepage.models import Coustomer
from django.contrib.auth.models import User
# Create your models here.


class OurWorkingCompany(models.Model):
    companyName=models.CharField(max_length=433,default=None)
    def __str__(self):
        return str(self.companyName)

class productCatagory(models.Model):
    name=models.CharField(max_length=100,default=1,blank=True,null=True)
    img=models.ImageField(upload_to='productCatagory',default=None,blank=True,null=True)
    def __str__(self):
        return str(self.name)

class Product(models.Model):
    title=models.CharField(max_length=100,default=None)
    mrp=models.FloatField(null=True,blank=True,default=0.0)
    our_price=models.FloatField(null=True,blank=True,default=0.0)
    product_catagory=models.ForeignKey(productCatagory,default=None,null=True,on_delete=models.CASCADE,blank=True)
    product_orgin=models.ForeignKey(OurWorkingCompany,default=None,null=True,on_delete=models.CASCADE,blank=True)
    product_img=models.ImageField(upload_to='productImg',default=None)
    def __str__(self):
        return str(self.title)
    
class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE,)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.user.username
    

STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)
class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customar=models.ForeignKey(Coustomer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending ')