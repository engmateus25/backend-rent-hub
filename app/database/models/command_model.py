from tortoise import fields
from tortoise.models import Model
import uuid

class Command(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    equipment_id = fields.UUIDField()
    payload = fields.CharField(max_length=200, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "commands"
