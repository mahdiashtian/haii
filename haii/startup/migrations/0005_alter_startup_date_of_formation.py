# Generated by Django 4.0.4 on 2022-07-05 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0004_remove_startup_ceo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='date_of_formation',
            field=models.DateTimeField(verbose_name='تاریخ تشکیل'),
        ),
    ]
