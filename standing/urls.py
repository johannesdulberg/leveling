from django.urls import path
from . import views
app_name = "standing"
urlpatterns = [
    path('skilltree/', views.index, name='index'),
    
]