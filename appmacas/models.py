from django.db import models

# Create your models here.
class Categorias(models.Model):
    id_categorias = models.AutoField(primary_key=True)
    imagen = models.ImageField(max_length=150, upload_to='categorias')
    # imagen_crop = ImageRatioField('imagen', '75x75', size_warning=True, free_crop=True)
    # imagen_crop_index = ImageRatioField('imagen', '400x133', size_warning=True)
    nombre = models.CharField(max_length=150)
    # descripcion = RichTextUploadingField(max_length=1000)
    precio = models.FloatField(default=40.00)

    class Meta:
    	verbose_name = 'Categoria'
    	verbose_name_plural = 'Categorias'
    	db_table = 'categorias'

    def __str__(self):
        return u'%s' %(self.nombre)