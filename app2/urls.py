from django.urls import path
from app2.views import *
app_name='yogi'

urlpatterns=[
    path('mama/',mama,name='mama')
]
