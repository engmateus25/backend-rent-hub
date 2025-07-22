from tortoise import fields
from tortoise.models import Model
from datetime import datetime, timezone
import uuid 


class User(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    name = fields.CharField(max_length=60)
    email = fields.CharField(max_length=60, unique=True)
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(default_factory=lambda: datetime.now(timezone.utc))

    class Meta:
        table = "users"    
