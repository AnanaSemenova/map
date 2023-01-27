from django.db import models


class Reviews(models.Model):
     text = models.TextField('Отзыв')

     def __str__(self):
         return self.text

     class Meta:
         verbose_name = 'Отзыв'
         verbose_name_plural = 'Отзывы'


class AdditionalUsers(models.Model):
    name_pol = models.TextField('Пользователи')
    mail = models.EmailField('Почта пользователя/организации')
    pas = models.TextField('Пароль')
    id_dev = models.IntegerField('Код прибора', max_length=20)

    def __str__(self):
        return self.name_pol

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

