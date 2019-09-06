from django.contrib import admin

from .models import Info, Paint, Technique, Publication
from .forms import InfoForm, PaintForm, TechniqueForm


@admin.register(Technique)
class TechniqueAdmin(admin.ModelAdmin):
    form = TechniqueForm
    exclude = ('image',)
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return obj.image.preview()


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    form = InfoForm
    exclude = ('image',)


@admin.register(Paint)
class PaintAdmin(admin.ModelAdmin):
    form = PaintForm
    exclude = ('image',)


admin.site.register(Publication)
