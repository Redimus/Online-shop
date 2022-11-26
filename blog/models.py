from django.db import models


class Post(models.Model):
    """Посты для блога"""
    title = models.CharField('Заголовок', max_length=150)
    description = models.TextField('Текст записи')
    photo = models.ImageField('Фото', upload_to='blog_photo', blank=True)
    publication_date = models.DateField('Дата публикации')
    is_published = models.BooleanField('Опубликовать', default=False)

