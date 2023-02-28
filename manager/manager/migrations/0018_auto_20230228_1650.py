# Generated by Django 2.2.17 on 2023-02-28 16:50

from django.db import migrations, models
import manager.models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0017_auto_20230228_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuration',
            name='content_aflatoun',
        ),
        migrations.AlterField(
            model_name='configuration',
            name='admin_password',
            field=models.CharField(default='admin-password', help_text='To manage KA-Lite, EduPi and Wikifundi', max_length=31, validators=[manager.models.validate_admin_pwd], verbose_name='Admin password'),
        ),
    ]
