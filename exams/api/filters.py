from django_filters import rest_framework as filters
from public.models import Tests


class TestsFilterSet(filters.FilterSet):
    class Meta:
        model = Tests
        fields = ("lab_id",)
