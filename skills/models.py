from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



class Skill(models.Model):
    name = models.CharField(max_length=100)
    skill_icon = models.URLField(max_length=100, null=True, blank=True)
    skill_description = models.CharField(max_length=400, null=True, blank=True)
    category = models.CharField(max_length=30)
    level = models.IntegerField(
        default=1, validators=[MaxValueValidator(10), MinValueValidator(1)]
    )

    def __str__(self):
        return self.name
