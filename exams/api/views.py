from api.filters import TestsFilterSet
from api.serializers import TestsSerializer
from django.db.models import F
from django_filters import rest_framework as dj_filters
from public.models import Tests
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class TestsViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = (
        Tests.objects.all()
        .exclude(completed_at__isnull=True)
        .annotate(duration_seconds=F("completed_at") - F("started_at"))
    )
    serializer_class = TestsSerializer
    filter_backends = (dj_filters.DjangoFilterBackend,)
    filterset_class = TestsFilterSet
