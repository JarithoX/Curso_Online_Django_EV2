from django.urls import path
from .views import homeView

#Vista/url por defecto
urlpatterns = [
    path('', homeView, name='home')
]
