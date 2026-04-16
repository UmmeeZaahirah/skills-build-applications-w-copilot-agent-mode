from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password'),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='password'),
        ]

        # Activities
        Activity.objects.create(user='ironman', activity_type='Running', duration=30, team='Marvel')
        Activity.objects.create(user='captainamerica', activity_type='Cycling', duration=45, team='Marvel')
        Activity.objects.create(user='batman', activity_type='Swimming', duration=60, team='DC')
        Activity.objects.create(user='superman', activity_type='Flying', duration=120, team='DC')

        # Workouts
        Workout.objects.create(name='Super Strength', description='Strength workout for heroes', difficulty='Hard')
        Workout.objects.create(name='Agility Training', description='Agility and speed drills', difficulty='Medium')

        # Leaderboard
        Leaderboard.objects.create(user='ironman', team='Marvel', points=100)
        Leaderboard.objects.create(user='captainamerica', team='Marvel', points=90)
        Leaderboard.objects.create(user='batman', team='DC', points=95)
        Leaderboard.objects.create(user='superman', team='DC', points=110)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
