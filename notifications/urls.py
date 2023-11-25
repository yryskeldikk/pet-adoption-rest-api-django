from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.NotificationManageViewSet, basename='notifications')

urlpatterns = [
    path('', include(router.urls)),
]
