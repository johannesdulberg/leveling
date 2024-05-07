# Generated by Django 4.2 on 2023-04-07 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tracker", "0005_training_date_unit_userthattrains"),
    ]

    operations = [
        migrations.RemoveField(model_name="training", name="Excercise",),
        migrations.RemoveField(model_name="unit", name="Date",),
        migrations.AlterField(
            model_name="training",
            name="userTraining",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
