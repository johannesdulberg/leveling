# Generated by Django 4.2 on 2024-05-12 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moves', '0020_remove_exercise_pre_requisit_to_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='progress',
            field=models.IntegerField(blank=True, choices=[(0, 'Never Tried'), (10, 'Tried in Lines'), (20, 'In Lines (5 seconds+)'), (30, 'With Spotters (5 s+)'), (40, 'In Lines (10 s+)'), (50, 'With Spotters (10 s+)'), (60, 'Out of Lines (10 s+)'), (70, 'Consistently Out of Lines with Multiple People (10 s+)'), (80, 'Consistently Out of Lines No Steps (10 s+)'), (90, 'Consistently Out of Lines No Steps with Multiple People (10 s+)'), (100, 'Mastered')], null=True),
        ),
    ]