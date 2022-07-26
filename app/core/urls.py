from rest_framework.routers import DefaultRouter

from .views import ApiViewSet

router = DefaultRouter()

router.register('v1/api', ApiViewSet, basename='api')
