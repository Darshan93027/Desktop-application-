from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/',views.login_view, name='login'),
    path('', views.index, name='index'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_data/', views.display_signup_data, name='admin_data'),
    path('login_success', views.main_page, name='main_page'),
    path('chatt/', views.chat, name='chatt'),
    path('help',views.help,name='help'),
    path('chat/', views.chat, name='chat'),
    path('msg/', views.chat_view, name='msg'),
    #yeh do line bhi likhi hai
    path('sender/', views.sender_view, name='sender'),
    path('receiver/', views.receiver_view, name='receiver'),
    path('gender/', views.gender_view, name='gender'),
    path('choose/', views.choose_view, name='choose'),
    path('learn_more/', views.learn_more_view, name='learn_more'),


     
     
]
