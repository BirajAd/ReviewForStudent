from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('sign_up', views.sign_up, name="sign_up"),
    path('logIn', views.logIn, name="logIn"),
    path('logOut', views.logOut, name="logOut"),
    path('myAccount', views.myAccount, name="myAccount"),
    path('business', views.business, name='business'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('checkBusiness', views.checkBusiness, name='checkBusiness'),
    path('<str:business_id>', views.postComment, name='postComment'),
    #path('loadApi', views.loadApi, name="loadApi"),
]
