import os
import uuid

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from utils.models import BaseModel


class Image(BaseModel):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        verbose_name=_("uuid"),
    )
    image = models.ImageField(
        upload_to='images',
        default='',
        max_length=200,
        verbose_name=_("Image File"),
    )
    position = models.SmallIntegerField(
        default=0,
        blank=True,
        verbose_name=_('Position'),
    )

    def __str__(self):
        return self.uuid.hex

    def clean(self, *args, **kwargs):
        if not self.image.name.endswith(self.uuid.hex):
            self.image.name = self.uuid.hex
        super().clean(*args, **kwargs)

    @property
    def image_url(self):
        return f"/media/images/{self.uuid.hex}"

    def address(self, request=None):
        url = self.image_url
        if request:
            url = request.build_absolute_uri(url)
        return mark_safe(f'<p dir="ltr">{url}</p>')

    def preview(self):
        return mark_safe(
            f"""
              <img src="{self.image_url}" style="max-height: 300px" />
            """
        )

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")
        ordering = ('position',)


@receiver(post_delete, sender=Image)
def image_post_delete(sender, instance, **kwargs):
    fpath = instance.image.path
    if os.path.exists(fpath):
        os.remove(fpath)
