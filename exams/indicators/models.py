from abstract_models.models import (AbstaractExamsModel,
                                    AbstaractIndicatorMetricsModel)
from django.db.models import SET_NULL, CharField, DecimalField, ForeignKey
from public.models import Tests


class Indicators(AbstaractIndicatorMetricsModel):
    class Meta:
        verbose_name = "Indicator"
        verbose_name_plural = "Indicators"


class Metrics(AbstaractIndicatorMetricsModel):
    unit = CharField(max_length=30)

    class Meta:
        verbose_name = "Metric"
        verbose_name_plural = "Metrics"


class IndicatorsMetrics(AbstaractExamsModel):
    indicator_id = ForeignKey(
        Indicators, on_delete=SET_NULL, null=True, related_name="metrics_indicators"
    )
    metric_id = ForeignKey(
        Metrics, on_delete=SET_NULL, null=True, related_name="indicators_metrics"
    )

    class Meta:
        verbose_name_plural = "indicators metrics"

    def __str__(self) -> str:
        return self.indicator_id.name + " " + self.metric_id.name


class Scores(AbstaractExamsModel):
    score = DecimalField(max_digits=9, decimal_places=5)
    test_id = ForeignKey(Tests, on_delete=SET_NULL, null=True, related_name="scores")
    indicator_metric_id = ForeignKey(IndicatorsMetrics, on_delete=SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Scores"

    def __str__(self) -> str:
        return str(self.score)


class References(AbstaractExamsModel):
    min_score = DecimalField(max_digits=6, decimal_places=2)
    max_score = DecimalField(max_digits=6, decimal_places=2)
    indicator_metric_id = ForeignKey(
        IndicatorsMetrics, on_delete=SET_NULL, null=True, related_name="references"
    )

    class Meta:
        verbose_name_plural = "References"

    def __str__(self) -> str:
        return str(self.min_score) + " " + str(self.max_score)
