from django.urls import path
from core import views

urlpatterns = [
    #MVC
    path('index/', views.index, name='index'), #view
    path('login/', views.login, name='login'), #view
    path('profile/', views.profile, name='profile'), #view
    path('editprofile/', views.editprofile, name='editprofile'), #view
    path('testapi/', views.testapi, name='testapi'), #view
    path('validatelogin/', views.validatelogin, name='validatelogin'), #controller
    path('updateprofile/', views.updateprofile, name='updateprofile'), #controller
    path('logout/', views.logout, name='logout'),#controller
    path('api/', views.api)
]
