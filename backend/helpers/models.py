from django.db import models
import uuid


class TrackingModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at  = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True