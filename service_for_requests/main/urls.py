from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RequestCreateViewSet, PingViewSet, HistoryViewSet, ResultRetrieveViewSet

router = DefaultRouter()
router.register('query', RequestCreateViewSet, basename='query')
router.register('result', ResultRetrieveViewSet, basename='result')
router.register('history', HistoryViewSet, basename='history')
router.register('ping', PingViewSet, basename='ping')


urlpatterns = [
    path('', include(router.urls)),
]
