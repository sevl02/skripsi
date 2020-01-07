from django.urls import path, include
from userweb import views

app_name = 'userweb'
urlpatterns = [
    path('', views.index, name='index'),
]