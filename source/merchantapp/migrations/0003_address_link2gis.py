# Generated by Django 3.2 on 2021-12-28 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchantapp', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='link2gis',
            field=models.URLField(default='https://2gis.kz/', verbose_name='Ссылка на 2GIS'),
            preserve_default=False,
        ),
    ]
