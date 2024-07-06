from django.contrib import admin
from .models import Coustomer
# Register your models here.

@admin.register(Coustomer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','nickname','city','ph']