from django.urls import path
from .views import home, menu, news, career, franchise, contact

urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('news/', news, name='news'),
    path('career/', career, name='career'),
    path('franchise/', franchise, name='franchise'),
    path('contact/', contact, name='contact'),
]
