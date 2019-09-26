from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from utils.models import SingletonModel, BaseModel


class Technique(BaseModel):
    name = models.CharField(max_length=100)
    image = models.OneToOneField(
        'gallery.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Paint(BaseModel):
    title = models.CharField(max_length=100)
    technique = models.ForeignKey(
        Technique,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='paints'
    )
    image = models.OneToOneField(
        'gallery.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    created_at = models.CharField(max_length=100,
                                  blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Info(SingletonModel):
    cv = RichTextUploadingField(
        default='',
        blank=True
    )
    statement = RichTextUploadingField(
        default='',
        blank=True
    )
    contact_text = RichTextUploadingField(
        default='',
        blank=True
    )
    image = models.OneToOneField(
        'gallery.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = 'Info'


class Publication(BaseModel):
    title = models.CharField(max_length=100)
    body = RichTextUploadingField()

    def __str__(self):
        return self.title
