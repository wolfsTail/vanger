from django.db import models
from users.models import CustomUser
from filer.fields.image import FilerImageField


class Slider(models.Model):
    title = models.CharField(
        max_length=128, verbose_name='Наименование'
        )
    image = FilerImageField(
        related_name='slider_images', on_delete=models.CASCADE, verbose_name='Изображение'
        )
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name='Владелец', editable=False
        )
    order = models.PositiveIntegerField(
        default=0, editable=False, db_index=True, verbose_name='Порядок сортировки'
        )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['order']
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
