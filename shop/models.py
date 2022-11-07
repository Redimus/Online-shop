from django.db import models


class Category(models.Model):
    """ Категории товаров """
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Товары """
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.SmallIntegerField()
    sale = models.SmallIntegerField(blank=True)
    photo_preview = models.ImageField(upload_to='product_photos/')
    photo_overview = models.ImageField(upload_to='product_photos/')
    is_published = models.BooleanField(default=False)
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title
