from django.db import models
from helpers.models import TrackingModel

# Create your models here.
class Todo(TrackingModel):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.title
