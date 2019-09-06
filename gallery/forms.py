from django import forms

from .models import Image


class ImageInlineModelForm(forms.ModelForm):
    is_m2m = False

    class Meta:
        model = Image
        fields = ('image_', )

    image_ = forms.ImageField(
        required=False,
        label=Image._meta.get_field('image').verbose_name,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.image_id:
            self.initial['image_'] = self.instance.image.image

    def save(self, *args, **kwargs):
        new_image = self.cleaned_data.get('image_', None)
        old_image = self.instance.image if self.instance.image_id else None
        new_position = self.cleaned_data.get('position_') or 0
        if not new_image:
            if old_image:
                self.instance.image.delete()
                self.instance.image = None
            if self.is_m2m:
                return
            else:
                return super().save(*args, **kwargs)

        if old_image:
            if hasattr(new_image, 'path') and \
               new_image.path == old_image.image.path:
                if self.is_m2m:
                    if self.instance.image.position != new_position:
                        self.instance.image.position = new_position
                        self.instance.image.save()
                return super().save(*args, **kwargs)
            else:
                old_image.delete()

        self.instance.image = Image.objects.create(
            image=self.cleaned_data['image_'],
            position=new_position,
        )

        return super().save(*args, **kwargs)


class ImageInlineM2MModelForm(ImageInlineModelForm):
    is_m2m = True
    position_ = forms.IntegerField(
        required=False,
        label='Position',
    )

    class Meta:
        model = Image
        fields = ('image_', 'position_')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.image_id:
            self.initial['position_'] = self.instance.image.position
