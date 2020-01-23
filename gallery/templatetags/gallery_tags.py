from uuid import UUID
from django import template


register = template.Library()


@register.simple_tag()
def image_url(uuid, width=None, height=None, image_type='contain'):
    if not uuid:
        return ''

    if isinstance(uuid, UUID):
        uuid = uuid.hex

    if not width and not height:
        return f'/image/{uuid}'

    if image_type not in ('cover', 'contain'):
        image_type = 'contain'

    width = f'/{width}' if width else ''
    height = f'/{height}' if height else ''
    image_type = f'/{image_type}' if image_type else ''

    return f'/image/{uuid}{width}{height}{image_type}'
