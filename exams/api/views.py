from api.filters import TestsFilterSet
from api.serializers import TestsSerializer
from django.db.models import F, OuterRef, Prefetch
from django_filters import rest_framework as dj_filters
from indicators.models import References, Scores
from public.models import Tests
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class TestsViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = TestsSerializer
    filter_backends = (dj_filters.DjangoFilterBackend,)
    filterset_class = TestsFilterSet

    def get_queryset(self):
        subquery = References.objects.filter(
            indicator_metric_id=OuterRef("indicator_metric_id")
        )
        manager_scores = Prefetch(
            "scores",
            queryset=Scores.objects.all()
            .select_related(
                "indicator_metric_id",
                "indicator_metric_id__indicator_id",
                "indicator_metric_id__metric_id",
            )
            .annotate(
                min_score=subquery.values("min_score"),
                max_score=subquery.values("max_score"),
            ),
        )

        queryset = (
            Tests.objects.all()
            .exclude(completed_at__isnull=True)
            .annotate(duration_seconds=F("completed_at") - F("started_at"))
            .prefetch_related(manager_scores)
        )
        return queryset
