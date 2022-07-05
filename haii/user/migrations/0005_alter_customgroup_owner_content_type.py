# Generated by Django 4.0.4 on 2022-07-05 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('user', '0004_alter_customgroup_owner_content_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customgroup',
            name='owner_content_type',
            field=models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'startup'), ('model', 'startup')), models.Q(('app_label', 'team'), ('model', 'team')), models.Q(('app_label', 'product'), ('model', 'product')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, related_name='owner_group_content_type', to='contenttypes.contenttype'),
        ),
    ]
