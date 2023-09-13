from django.contrib import admin
from public.models import Labs, Tests


@admin.register(Labs)
class LabsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "created_at",
        "updated_at",
    )


@admin.register(Tests)
class TestsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "started_at",
        "completed_at",
        "comment",
        "lab_id",
        "is_active",
        "created_at",
        "updated_at",
    )
