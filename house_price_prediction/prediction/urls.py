from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('features',views.features, name='features'),
    path('predict/', views.predict, name='predict'),
]
