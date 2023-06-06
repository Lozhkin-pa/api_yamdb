from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, create_token, create_user

app_name = 'api'

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', create_user, name='create_user'),
    path('v1/auth/token/', create_token, name='create_token'),
]