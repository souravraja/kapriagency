
from django.urls import path,include
from . import views
urlpatterns=[
    path("company/",views.companyname),
]
