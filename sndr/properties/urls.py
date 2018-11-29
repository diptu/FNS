from django.urls import path
from .views import *


urlpatterns = [

    path('create/', AdCreate.as_view(), name='ad_create'),
    path('', AdListView.as_view(), name='ad_list'),
    path('<slug:slug>/', AdDetailView.as_view(), name='ad_detail'),
    path('<slug:slug>/update', AdUpdate.as_view(), name='ad_update'),
    path('<slug:slug>/delete', AdDelete.as_view(), name='ad_detete'),

]
