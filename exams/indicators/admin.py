from django.contrib import admin
from indicators.models import (Indicators, IndicatorsMetrics, Metrics,
                               References, Scores)
from public.models import Labs, Tests


@admin.register(Indicators)
class IndicatorsAdmin(admin.ModelAdmin):
    pass


@admin.register(Metrics)
class MetricsAdmin(admin.ModelAdmin):
    pass


@admin.register(IndicatorsMetrics)
class IndicatorsMetricsAdmin(admin.ModelAdmin):
    pass


class LabsInline(admin.TabularInline):
    model = Labs
    readonly_fields = ("id",)
    extra = 1


class TestsInline(admin.TabularInline):
    inlines = (LabsInline,)
    model = Tests
    readonly_fields = ("id",)
    extra = 1


@admin.register(References)
class ReferencesAdmin(admin.ModelAdmin):
    pass


@admin.register(Scores)
class ScoresAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "score",
        "test_id",
        # "started_at",
        # "completed_at",
        "is_active",
        "created_at",
        "updated_at",
    )
