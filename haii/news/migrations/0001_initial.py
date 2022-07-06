# Generated by Django 4.0.4 on 2022-07-06 07:47

from django.db import migrations, models
import django.db.models.deletion
import utils.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ['id'],
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
            ],
            options={
                'verbose_name': 'برچسب',
                'verbose_name_plural': 'برچسب ها',
                'ordering': ['id'],
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('news', models.TextField(verbose_name='خبر')),
                ('image', models.ImageField(blank=True, null=True, upload_to=utils.utils.upload_image_path, verbose_name='تصویر')),
                ('date_of_registration', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('edit_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('share', models.BooleanField(default=False, verbose_name='اشتراک گذاری در شبکه های اجتماعی')),
                ('date_of_send', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ ارسال به کانال تلگرام')),
                ('category', models.ManyToManyField(blank=True, to='news.category', verbose_name='دسته بندی')),
                ('tag', models.ManyToManyField(blank=True, to='news.tag', verbose_name='تگ')),
            ],
            options={
                'verbose_name': 'خبر',
                'verbose_name_plural': 'خبر ها',
                'ordering': ['date_of_registration'],
                'base_manager_name': 'objects',
            },
        ),
    ]
