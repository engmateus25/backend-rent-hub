from tortoise import fields
from tortoise.models import Model
from datetime import datetime, timezone
import uuid


class ReservationStatus(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    name = fields.CharField(max_length=60, unique=True)
    created_at = fields.DatetimeField(default_factory=lambda: datetime.now(timezone.utc))

    class Meta:
        table = "reservation_statuses"
