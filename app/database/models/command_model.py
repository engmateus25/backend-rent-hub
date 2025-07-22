from tortoise import fields
from tortoise.models import Model
from datetime import datetime, timezone
import uuid


class Command(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    equipment_id = fields.UUIDField()
    payload = fields.CharField(max_length=200, null=True)
    created_at = fields.DatetimeField(default_factory=lambda: datetime.now(timezone.utc))

    class Meta:
        table = "commands"
