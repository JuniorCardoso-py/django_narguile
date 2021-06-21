from django.db import models
from base.models import BaseModel

# Create your models here.
class Narguile(BaseModel):

    name = models.CharField(max_length=80)
    price = models.FloatField()
    heitgt_type = models.CharField(max_length=30)
    stock = models.IntegerField()

