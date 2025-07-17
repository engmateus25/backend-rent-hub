from tortoise import fields
from tortoise.models import Model
import uuid


class ReservationStatus(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    name = fields.CharField(max_length=60, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "reservation_statuses"
