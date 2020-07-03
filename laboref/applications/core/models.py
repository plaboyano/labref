from django.db import models

"""
# definiendo donde y como se suben las imagenes de cada item
def custom_upload_to_(instance, filename):
    old_instance = ItemSlider.objects.get(pk=instance.pk)
    if old_instance:
        old_instance.image.delete()
    return 'itemsSlider/' + filename
"""


class ItemSlider(models.Model):
    title = models.CharField(null=False, blank=False, verbose_name='Titulo', max_length=20)
    description = models.TextField(null=False, blank=False, verbose_name='Descripcion', max_length=50)
    image = models.ImageField(upload_to="itemsSlider", null=True, blank=True)
    order = models.SmallIntegerField(verbose_name="Orden", default=0)

    class Meta:
        verbose_name = "Item deslizador"
        verbose_name_plural = "Items del deslizador"
        ordering = ['order']

    def __str__(self):
        return self.title
