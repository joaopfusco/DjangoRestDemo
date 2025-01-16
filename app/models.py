from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
class ItemModel(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    
    class Meta:
        verbose_name = "item"
        verbose_name_plural = "itens"
