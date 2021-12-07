from django.urls.conf import path
from . import views

urlpatterns = [
    
    path('serve2/',views.serve,name='serv'),
]