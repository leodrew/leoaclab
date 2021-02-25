from django.conf.urls import include
from acapp import views
from django.urls import path


app_name = 'acapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('user_login',views.user_login,name="user_login"),
    path('postblog',views.postblog,name='post_blog')
]
