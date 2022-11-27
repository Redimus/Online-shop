from django.db import models


class Category(models.Model):
    """ Категории товаров """
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', null=True)
    slug = models.SlugField(max_length=160, null=True)
    photo = models.ImageField('Фото', upload_to='category_photos/', null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Товары """
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', null=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    price = models.SmallIntegerField('Цена')
    sale = models.SmallIntegerField('Скидка (новая цена)', null=True, blank=True)
    photo_preview = models.ImageField('Основное фото', upload_to='product_photos/')
    photo_overview = models.ImageField('Дополнительные фото', upload_to='product_photos/')
    is_published = models.BooleanField('Опубликовать', default=False)
    available = models.BooleanField('В наличии', default=False)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title
