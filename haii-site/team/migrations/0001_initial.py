# Generated by Django 4.0.4 on 2022-07-07 10:41

from django.conf import settings
from django.db import migrations, models
import utils.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('image', models.ImageField(blank=True, null=True, upload_to=utils.utils.upload_image_path, verbose_name='لوگو')),
                ('date', models.DateTimeField(verbose_name='سال ساخت')),
                ('user', models.ManyToManyField(related_name='user_team', to=settings.AUTH_USER_MODEL, verbose_name='اعضا')),
            ],
            options={
                'verbose_name': 'تیم',
                'verbose_name_plural': 'تیم ها',
                'ordering': ['id'],
                'base_manager_name': 'objects',
            },
        ),
    ]
