from tortoise import fields
from tortoise.models import Model
import uuid

class Reservation(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    user_id = fields.UUIDField()
    equipment_id = fields.UUIDField()
    start_time = fields.DatetimeField()
    end_time = fields.DatetimeField()
    status_id = fields.UUIDField()
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "reservations"
