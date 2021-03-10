from django.urls import path
from .views import Like

urlpatterns = [
    path('like/', Like.as_view(), name='LikePage'),
]
