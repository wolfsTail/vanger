from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableAdminMixin

from slider.models import Slider


class SliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('order', 'title', 'owner', 'image_tag')
    list_display_links = ('title', 'image_tag')
    list_select_related = ('owner',)
    readonly_fields = ('image_tag', 'owner')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px;" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Изображение'
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.owner = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Slider, SliderAdmin)
