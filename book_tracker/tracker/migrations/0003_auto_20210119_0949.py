# Generated by Django 3.1.5 on 2021-01-19 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20210119_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_name',
            field=models.CharField(max_length=100, verbose_name='Автор'),
        ),
    ]
