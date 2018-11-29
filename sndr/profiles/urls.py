from django.urls import path

from .views import *
urlpatterns = [

    path('signup/', signup, name='signup'),
    path('<pk>/', UserDetailView.as_view(), name='user_detail'),

]
