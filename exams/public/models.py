from abstract_models.models import AbstaractExamsModel
from django.db.models import SET_NULL, CharField, DateTimeField, ForeignKey


class Labs(AbstaractExamsModel):
    name = CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Labs"

    def __str__(self) -> str:
        return self.name


class Tests(AbstaractExamsModel):
    started_at = DateTimeField(default=None, null=True, blank=True)
    completed_at = DateTimeField(default=None, null=True, blank=True)
    comment = CharField(max_length=300, null=True, blank=True, default=None)
    lab_id = ForeignKey(Labs, on_delete=SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Tests"

    def __str__(self) -> str:
        return self.comment if self.comment else str(self.id)
