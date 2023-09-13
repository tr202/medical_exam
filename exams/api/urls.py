from api.views import TestsViewSet  # ,ScoresViewSet
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()

router.register("tests", TestsViewSet, basename="tests")
# router.register("scores", ScoresViewSet, basename="scores")

urlpatterns = [
    path("", include(router.urls)),
]
