from tortoise import fields
from tortoise.models import Model
from datetime import datetime, timezone
import uuid


class EquipmentStatusLog(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    status_id = fields.UUIDField()
    equipment_id = fields.UUIDField()
    details = fields.CharField(max_length=300)
    reported_at = fields.DatetimeField(auto_now_add=True)
    created_at = fields.DatetimeField(default_factory=lambda: datetime.now(timezone.utc))

    class Meta:
        table = "equipment_status_logs"
