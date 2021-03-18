from django.urls import path
from .views import Register, Auth, UserLK, Logout

urlpatterns = [
    path('register/', Register.as_view(), name='RegisterPage'),
    path('login/', Auth.as_view(), name='AuthPage'),
    path('user/', UserLK.as_view(), name='UserPage'),
    path('logout/', Logout.as_view(), name='Logout'),
]
