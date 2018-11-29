from django.urls import path
from .views import *


urlpatterns = [

    path('<slug:slug>/', BookingView.as_view(), name='booking'),

]
