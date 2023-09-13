import uuid

import pgtrigger
from django.db.models import (BooleanField, CharField, DateTimeField, Model,
                              UUIDField)


class AbstaractExamsModel(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_active = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(null=True, blank=True, default=None)

    class Meta:
        abstract = True
        triggers = [
            pgtrigger.Trigger(
                name="catch_update_timestamp",
                operation=pgtrigger.Update,
                when=pgtrigger.Before,
                func="NEW.updated_at = now(); RETURN NEW;",
            )
        ]


class AbstaractIndicatorMetricsModel(AbstaractExamsModel):
    name = CharField(max_length=100)
    description = CharField(max_length=300)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name
