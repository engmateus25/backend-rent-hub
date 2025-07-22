from tortoise import fields
from tortoise.models import Model
from datetime import datetime, timezone
import uuid

class UserAuth(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    username = fields.CharField(max_length=60, unique=True)
    password_hash = fields.CharField(max_length=100)
    user_id = fields.UUIDField()
    created_at = fields.DatetimeField(default_factory=lambda: datetime.now(timezone.utc))

    class Meta:
        table = "user_auth"
