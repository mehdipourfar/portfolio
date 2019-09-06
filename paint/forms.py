from .models import Technique, Paint, Info

from gallery.forms import ImageInlineModelForm


class TechniqueForm(ImageInlineModelForm):
    class Meta:
        model = Technique
        fields = '__all__'


class PaintForm(ImageInlineModelForm):
    class Meta:
        model = Paint
        fields = '__all__'


class InfoForm(ImageInlineModelForm):
    class Meta:
        model = Info
        fields = '__all__'
