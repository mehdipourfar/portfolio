from django.db import models
from utils.models import SingletonModel, BaseModel


class Technique(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Paint(BaseModel):
    title = models.CharField(max_length=100)
    technique = models.ForeignKey(
        Technique,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    photo = models.ImageField(max_length=100)
    created_at = models.CharField(max_length=100,
                                  blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Info(SingletonModel):
    cv = models.TextField(
        default='',
        blank=True
    )
    statement = models.TextField(
        default='',
        blank=True
    )
    contact_text = models.TextField(
        default='',
        blank=True
    )
    home_repetitive_image = models.ImageField(
        max_length=100,
        blank=True,
    )
