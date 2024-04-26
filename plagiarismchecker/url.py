from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='plagiarism-check-mainpage'),
    path('compare/', views.fileCompare,name='compare'), 
    path('test/', views.test,name='Test'),
    path('filetest/', views.filetest,name='filetest'),
    path('twofiletest1/', views.twofiletest1,name='twofiletest1'),
    path('twofilecompare1/', views.twofilecompare1,name='twofilecompare1'),
    path('', views.home, name='home'),
    path('register/', views.registration_view, name='registerView'),
    path('login/', views.loginView, name='loginView'),
    path('index/', views.index_view, name='indexView'),
]
