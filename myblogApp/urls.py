from django.urls import path
from . import views

app_name = 'myblogApp'
urlpatterns = [
    path('myblogApp', views.index, name='index'),
    path('signup',views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('signout',views.signout, name='signout'),
    #path('myblogApp/<int:article_id>/add_comment/', add_comment,name='add_comment'),
]