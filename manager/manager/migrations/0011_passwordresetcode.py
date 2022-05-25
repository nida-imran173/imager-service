# Generated by Django 2.2.16 on 2020-11-11 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0010_auto_20201110_1543"),
    ]

    operations = [
        migrations.CreateModel(
            name="PasswordResetCode",
            fields=[
                ("code", models.UUIDField(primary_key=True, serialize=False)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="passwordresets",
                        to="manager.Profile",
                    ),
                ),
            ],
        ),
    ]
