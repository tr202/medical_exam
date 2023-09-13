from django.contrib.auth import get_user_model
from indicators.models import References, Scores
from public.models import Tests
from rest_framework import serializers

User = get_user_model()


class ScoresSerializer(serializers.ModelSerializer):
    metric_name = serializers.SerializerMethodField()
    metric_unit = serializers.SerializerMethodField()
    is_within_normal_range = serializers.SerializerMethodField()

    def get_metric_name(self, obj) -> str:
        return obj.indicator_metric_id.indicator_id.name

    def get_metric_unit(self, obj) -> str:
        return obj.indicator_metric_id.metric_id.name

    def get_is_within_normal_range(self, obj) -> bool:
        references = References.objects.get(indicator_metric_id=obj.indicator_metric_id)
        return references.min_score <= obj.score and obj.score <= references.max_score

    class Meta:
        model = Scores
        fields = (
            "id",
            "score",
            "metric_name",
            "metric_unit",
            "is_within_normal_range",
        )


class TestsSerializer(serializers.ModelSerializer):
    results = ScoresSerializer(many=True, source="scores_set")
    duration_seconds = serializers.SerializerMethodField()

    def get_duration_seconds(self, obj) -> int:
        return int(obj.duration_seconds.total_seconds())

    class Meta:
        model = Tests
        fields = (
            "id",
            "lab_id",
            "duration_seconds",
            "results",
        )
