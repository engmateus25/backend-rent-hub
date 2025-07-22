from tortoise import fields
from tortoise.models import Model
from datetime import datetime, timezone
import uuid


class Reservation(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    user_id = fields.UUIDField()
    equipment_id = fields.UUIDField()
    start_time = fields.DatetimeField(tz=True)
    end_time = fields.DatetimeField(tz=True)
    status_id = fields.UUIDField()
    created_at = fields.DatetimeField(default_factory=lambda: datetime.now(timezone.utc))

    class Meta:
        table = "reservations"
