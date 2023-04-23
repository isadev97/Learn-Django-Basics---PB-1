from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import Choices

# Create your models here.
class Todo(models.Model):
    STATUS_CHOICES = Choices(
        (1, "pending", _("pending")),
        (2, "completed", _("completed")),
    )
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    status = models.IntegerField(default=STATUS_CHOICES.pending)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table="todos"
        
        