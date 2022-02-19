from django.urls import path,include
from .views import HomePageView
from discord_bot import views

urlpatterns = [
    
    path('', HomePageView.as_view(),name='home'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),

]
