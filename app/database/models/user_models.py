from tortoise import fields
from tortoise.models import Model
import uuid 

class User(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    name = fields.CharField(max_length=60)
    email = fields.CharField(max_length=60, unique=True)
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=true)

    class Meta:
        table = "users"    
