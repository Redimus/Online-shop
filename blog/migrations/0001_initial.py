# Generated by Django 4.1.3 on 2022-11-26 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Текст записи')),
                ('photo', models.ImageField(blank=True, upload_to='blog_photo', verbose_name='Фото')),
                ('publication_date', models.DateField(verbose_name='Дата публикации')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовать')),
            ],
        ),
    ]
