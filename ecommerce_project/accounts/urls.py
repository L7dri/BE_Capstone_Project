from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, login, logout
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('api/auth/login/', obtain_auth_token, name='api_token_auth'),

]
