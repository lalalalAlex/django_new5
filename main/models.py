from django.db import models


class News(models.Model):
    title = models.CharField('Название', max_length=25)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comments(models.Model):
    name = models.CharField('Имя', max_length=25)
    description = models.TextField('Коментарий')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

