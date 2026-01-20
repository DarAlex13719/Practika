from django.urls import path
from .views import *

urlpatterns = [
   path('', com),
   path('thanks/', thanks, name='thanks'),
]