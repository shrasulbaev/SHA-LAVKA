# Generated by Django 4.1.7 on 2023-05-19 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shashop', '0002_product_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_favorite', models.BooleanField(default=False, verbose_name='избранный')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='shashop.product', verbose_name='товар')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Избранный товар',
                'verbose_name_plural': 'Избранные товары',
            },
        ),
    ]
