from rest_framework.routers import DefaultRouter

from .views import ApiViewSet

router = DefaultRouter(trailing_slash=False)

router.register('v1/api', ApiViewSet, basename='api')
