from django.contrib import admin

from .models import Image
from .forms import ImageInlineM2MModelForm

from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)


# @admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = (
        'preview',
        'address',
    )

    def get_fields(self, request, obj=None):
        self.request = request
        fields = ['address']
        fields.append('image' if obj is None else 'preview')
        return fields

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def address(self, instance):
        return instance.address(self.request)


class ManyToManyImageInline(admin.TabularInline):
    can_delete = False
    form = ImageInlineM2MModelForm
    fields = (
        'image_',
        'position_',
        'preview'
    )
    readonly_fields = ('preview',)

    def preview(self, obj):
        return obj.image.preview()


def m2m_image_inline(model):
    return type('', (ManyToManyImageInline,), {'model': model})
