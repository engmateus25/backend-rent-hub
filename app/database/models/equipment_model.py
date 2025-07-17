from tortoise import fields
from tortoise.models import Model
import uuid


class Equipment(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    name = fields.CharField(max_length=60, unique=True)
    current_status_id = UUIDField()
    is_activate = fields.BooleanField(default=True)
    last_heartbeat = fieldsDatetimeField()
    created_at = fields.DatetimeField(auto_now_add=true)

    class Meta:
        table = "equipments"    
