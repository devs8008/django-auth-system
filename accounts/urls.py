from django.urls import path, include


urlpatterns =[
    path('', include('django.contib.auth.urls'))
]