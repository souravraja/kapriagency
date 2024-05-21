from django.db import models
from django.contrib.auth.models import User
# Create your models here.
OurWorkingCompany=(
    ('prime','prime'),
    ('applo','applo'),
    ('ITC','ITC'),
    ('Dona','Dona'),
    ('',''),
    ('',''),
    ('',''),
    ('',''),
    ('',''),
    ('',''),
    ('',''),
    ('',''),
    ('',''),
    ('',''),

)
OurProductType=(
    ('pickl','pickl'),
    ('',''),
    ('',''),
)

class Product(models.Model):
    title=models.CharField(max_length=100,default=None)
    mrp=models.FloatField(null=True,blank=True,default=0.0)
    our_price=models.FloatField(null=True,blank=True,default=0.0)
    Product_type=models.CharField(choices=OurProductType,max_length=64,default=None)
    product_orgin=models.CharField(choices=OurWorkingCompany,max_length=64,default=None)
    product_img=models.ImageField(upload_to='productImg',default=None)
    def __str__(self):
        return str(self.title)
    
class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE,default=None)
    quantity=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username