from django.urls import path
from . import views
app_name = 'patient_app'
urlpatterns = [
    path('', views.patient_index,name='index'),
    path('about',views.about,name='about'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('what_is_bms',views.bms_details,name='what_is_bms'),
  

    
   
   
]
