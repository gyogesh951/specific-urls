from django.urls import path
from app1.views import *
app_name='abhi'

urlpatterns=[
    path('macha/',macha,name='macha'),
]
