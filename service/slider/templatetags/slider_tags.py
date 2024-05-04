from django import template
from easy_thumbnails.files import get_thumbnailer

register = template.Library()

@register.filter
def thumbnail_url(image_field, alias='default'):
    thumbnail_options = {'size': (165, 165), 'crop': 'smart'}
    if not image_field:
        return ""
    return get_thumbnailer(image_field).get_thumbnail(thumbnail_options).url