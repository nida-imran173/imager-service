# Generated by Django 2.2.16 on 2020-10-16 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0004_auto_20200312_1557"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organization",
            name="public_warehouse",
            field=models.CharField(
                choices=[("download", "download"), ("kiwix", "kiwix")],
                default="download",
                max_length=50,
                verbose_name="Pub WH",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="warehouse",
            field=models.CharField(
                choices=[("download", "download"), ("kiwix", "kiwix")],
                default="kiwix",
                max_length=50,
            ),
        ),
    ]
