from django.urls import path

from . import views

from django.conf.urls import include

app_name="main"

urlpatterns = [
    #/main/landing
    path('landing/', views.landing, name='landing'),
    #/main/order
    path('order/', views.order, name='order'),
    #/main/handle
    path('handle/', views.handle, name='handle'),
]
