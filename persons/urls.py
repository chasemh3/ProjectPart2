from django.urls import path 
from .views import indexPageView, kidsTable

urlpatterns = [
    path('', indexPageView),
    path('kids', kidsTable)
]
