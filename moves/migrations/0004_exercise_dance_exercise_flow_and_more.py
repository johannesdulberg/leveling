# Generated by Django 4.2 on 2023-04-17 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("moves", "0003_remove_exercise_muscle_groups_exercise_importance_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="exercise",
            name="dance",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="exercise",
            name="flow",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="exercise",
            name="washing_machine",
            field=models.BooleanField(default=False),
        ),
    ]
