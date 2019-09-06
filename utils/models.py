from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True


class SingletonModel(BaseModel):
    def clean(self, *args, **kwargs):
        super().clean(*args, **kwargs)
        if not self.pk and self._meta.model.objects.exists():
            raise ValidationError(
                _("This model can only have one object!")
            )

    def __str__(self):
        return str(self._meta.verbose_name)

    class Meta:
        abstract = True
