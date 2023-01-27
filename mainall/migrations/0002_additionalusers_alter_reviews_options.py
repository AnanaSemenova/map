# Generated by Django 4.1.2 on 2023-01-27 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainall', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_pol', models.TextField(verbose_name='Пользователи')),
                ('mail', models.EmailField(max_length=254, verbose_name='Почта пользователя/организации')),
                ('pas', models.TextField(verbose_name='Пароль')),
                ('id_dev', models.IntegerField(max_length=20, verbose_name='Код прибора')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]