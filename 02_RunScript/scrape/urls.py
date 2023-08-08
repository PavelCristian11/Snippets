from django.urls import path
from .views import HomeView, vehicleData
# from .views import HomeView 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('vehicle/', vehicleData, name='vehicleData')
]