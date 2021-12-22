from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =  [ 
    path('', views.index, name = 'index'),
    path('vote/<str:pk>', views.vote, name='vote'),
    path('result/<str:pk>', views.result, name = 'result'),
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('signup', views.signup, name='signup'),
    path('final/<str:pk>', views.final, name = 'final'),

    #path('signup', views.signup, name='signup'),
    #path('footer', views.footer, name = 'footer')
]
   
