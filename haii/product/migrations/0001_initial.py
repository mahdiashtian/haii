# Generated by Django 4.0.4 on 2022-07-05 10:13

from django.db import migrations, models
import django.db.models.deletion
import utils.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('image', models.ImageField(blank=True, null=True, upload_to=utils.utils.upload_image_path, verbose_name='لوگو')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='سال ساخت')),
                ('owner_object_id', models.PositiveIntegerField()),
                ('owner_content_type', models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'startup'), ('model', 'startup')), models.Q(('app_label', 'team'), ('model', 'team')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, related_name='owner_product_content_type', to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
                'ordering': ['date'],
                'base_manager_name': 'objects',
            },
        ),
    ]