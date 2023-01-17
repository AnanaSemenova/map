from django.db import models


class Reviews(models.Model):
     text = models.TextField('Отзыв')

     def __str__(self):
         return self.text

     class Meta:
         verbose_name = 'Отзыв'
         verbose_name_plural = 'Отзывы'



