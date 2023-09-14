from indicators.models import Scores
from public.models import Tests
from rest_framework import serializers


class ScoresSerializer(serializers.ModelSerializer):
    metric_name = serializers.SerializerMethodField()
    metric_unit = serializers.SerializerMethodField()
    is_within_normal_range = serializers.SerializerMethodField()

    def get_metric_name(self, obj) -> str:
        return obj.indicator_metric_id.indicator_id.name

    def get_metric_unit(self, obj) -> str:
        return obj.indicator_metric_id.metric_id.name

    def get_is_within_normal_range(self, obj) -> bool:
        return obj.min_score <= obj.score and obj.score <= obj.max_score

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
    results = ScoresSerializer(many=True, source="scores")
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
