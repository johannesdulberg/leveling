# Generated by Django 4.2 on 2023-04-06 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tracker", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Training",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Excercise", models.TextField()),
                (
                    "author",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(name="Profile",),
    ]