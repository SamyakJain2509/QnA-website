from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.index,name='index'),
    path('questions/',views.question_list,name='questions'),
    path('questions/ask/',views.ask,name='ask'),
    path('questions/<str:pk>/',views.question_detail,name='question_detail'),
]