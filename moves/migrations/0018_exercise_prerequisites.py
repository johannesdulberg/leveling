# Generated by Django 4.2 on 2024-05-12 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moves', '0017_exercise_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='prerequisites',
            field=models.ManyToManyField(blank=True, related_name='leads_to', to='moves.exercise'),
        ),
    ]
