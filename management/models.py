from asyncore import write
from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
import os
from django.utils.html import mark_safe



class BarCodeModel(models.Model):
    title = models.CharField(max_length=200, help_text='نام کالا')
    isbn = models.CharField('ISBN', max_length=13, help_text='کالا کد')
    barcode = models.ImageField(
        blank=True, null=True, upload_to='book_image', help_text='به این قسمت کاری نداشته باشید')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" width="200" height="100"/>'.format(self.barcode.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def save(self, *args, **kwargs):
        CODE_39 = barcode.get_barcode_class('code39')
        code = CODE_39(f'{self.isbn}', writer=ImageWriter(),
                       add_checksum=False)
        buffer = BytesIO()
        code.write(buffer)
        self.barcode.save('isbn.png', File(buffer), save=False)
        return super().save(*args, **kwargs)



