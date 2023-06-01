from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (CommentViewSet, ReviewViewSet)


app_name = 'api'
router = SimpleRouter()

router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)

urlpatterns = [
    path('v1/', include(router.urls)),
]