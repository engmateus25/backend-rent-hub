from tortoise from fields
from tortoise.models import Model
import uuid


class EquipmentStatusLog(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    status_id = fields.UUIDField()
    equipment_id = fields.UUIDField()
    details = fields.CharField(max_length=300)
    reported_at = fieldsDatetimeField(auto_now_add=True)
    created_at = fieldsDatetimeField(auto_now_add=True)

    class Meta:
        table = "equipment_status_logs"
