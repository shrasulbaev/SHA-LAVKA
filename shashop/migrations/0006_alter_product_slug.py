# Generated by Django 4.1.7 on 2023-05-19 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shashop', '0005_alter_orderitem_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='ссылка на товар'),
        ),
    ]
