from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model

class Human(User):
    age = models.PositiveIntegerField(

    )
