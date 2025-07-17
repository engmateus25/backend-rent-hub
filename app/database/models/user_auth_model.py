from tortoise import fields
from tortoise.models import Model
import uuid

class UserAuth(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    username = fields.CharField(max_length=60, unique=True)
    password_hash = fields.CharField(max_length=100)
    user_id = fields.UUIDField()
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "user_auth"
