from django.db import models
from django.conf import settings
from authuser.models import User
# class Transition(models.Model):
#    from_position = models.ForeignKey("Exercise", related_name='from_transitions',
#                                      on_delete=models.CASCADE, limit_choices_to={'position': True})
#    to_position = models.ForeignKey('Exercise', related_name='to_transitions',
#                                    on_delete=models.CASCADE, limit_choices_to={'position': True})
#
#    def __str__(self):
#        return f'{self.from_position} -> {self.to_position}'


class Exercise(models.Model):
    DIFFICULTY_CHOICES = (
        ('easy', 'Easy'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    )
    BASE_CHOICES = (
        ('lbase', 'L-Base'),
        ('standing', 'Standing'),
    )
    TYPE_CHOICES = (
        ('essential', 'Essential'),
        ('not_essential', 'Not Essential'),
    )
    PROGRESS_CHOICES = (
        (0, 'Never Tried'),
        (10, 'Tried in Lines'),
        (20, 'In Lines (5 seconds+)'),
        (30, 'With Spotters (5 s+)'),
        (40, 'In Lines (10 s+)'),
        (50, 'With Spotters (10 s+)'),
        (60, 'Out of Lines (10 s+)'),
        (70, 'Consistently Out of Lines with Multiple People (10 s+)'),
        (80, 'Consistently Out of Lines No Steps (10 s+)'),
        (90, 'Consistently Out of Lines No Steps with Multiple People (10 s+)'),
        (100, 'Mastered')
    )

    progress = models.IntegerField(choices=PROGRESS_CHOICES, null=True, blank=True)


    name = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=100, choices=DIFFICULTY_CHOICES)
    base = models.CharField(max_length=100, choices=BASE_CHOICES)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    image = models.ImageField(upload_to='exercise_images/', blank=True, null=True)
    dance = models.BooleanField(default=False)
    washing_machines = models.BooleanField(default=False)
    flows = models.BooleanField(default=False)
    whips = models.BooleanField(default=False)
    pops = models.BooleanField(default=False)
    counterbalance = models.BooleanField(default=False)
    position = models.BooleanField(default=False)
    static = models.BooleanField(default=False)
    variation = models.ForeignKey('self', null=True, blank=True, related_name='variations',
                                  on_delete=models.CASCADE, limit_choices_to={'position': True})

    entrance_from = models.ForeignKey('self', null=True, blank=True, related_name='entrance_from_exercises',
                                      on_delete=models.SET_NULL, limit_choices_to={'position': True})
    entrance_to = models.ForeignKey('self', null=True, blank=True, related_name='entrance_to_exercises',
                                    on_delete=models.SET_NULL, limit_choices_to={'position': True})
    exit_from = models.ForeignKey('self', null=True, blank=True, related_name='exit_from_exercises',
                                  on_delete=models.SET_NULL, limit_choices_to={'position': True})
    exit_to = models.ForeignKey('self', null=True, blank=True, related_name='exit_to_exercises',
                                on_delete=models.SET_NULL, limit_choices_to={'position': True})
    transition_from = models.ForeignKey('self', null=True, blank=True, related_name='transition_from_exercises',
                                        on_delete=models.SET_NULL, limit_choices_to={'position': True})
    transition_to = models.ForeignKey('self', null=True, blank=True, related_name='transition_to_exercises',
                                      on_delete=models.SET_NULL, limit_choices_to={'position': True})
    prerequisites = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='leads_to',limit_choices_to={'static': True})
    legit = models.BooleanField(default=False)
    video_url = models.URLField()

    def __str__(self):
        return self.name

class UserExerciseProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='exercise_progress')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='user_progress')
    progress = models.IntegerField(choices=User.PROGRESS_CHOICES, default=0)
    
    class Meta:
        unique_together = ('user', 'exercise')  # Ensures one entry per user-exercise pair

    def __str__(self):
        return f'{self.user.name} - {self.exercise.name} - Progress: {self.get_progress_display()}'