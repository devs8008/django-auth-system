from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.HomePageView.as_view(), name = 'home'),
    path('signup/', views.SignUpView.as_view(), name = 'signup')
]
