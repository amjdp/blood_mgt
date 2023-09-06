from django.urls import path
from . import views
app_name = 'common_app'

urlpatterns = [
    path('home', views.common_index,name='index'),
    path('about',views.about,name='about'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('what_is_bms',views.bms_details,name='what_is_bms'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('taluk',views.taluk,name='taluk')
   
   
]
