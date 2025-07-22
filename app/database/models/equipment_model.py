from tortoise import fields
from tortoise.models import Model
from datetime import datetime, timezone
import uuid


class Equipment(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    name = fields.CharField(max_length=60, unique=True)
    current_status_id = fields.UUIDField()
    is_activate = fields.BooleanField(default=True)
    last_heartbeat = fields.DatetimeField(tz=True)
    created_at = fields.DatetimeField(default_factory=lambda: datetime.now(timezone.utc))

    class Meta:
        table = "equipments"    
