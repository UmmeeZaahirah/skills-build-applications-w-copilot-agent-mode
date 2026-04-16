
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Team, Activity, Workout, Leaderboard

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'email']

class TeamSerializer(serializers.ModelSerializer):
	class Meta:
		model = Team
		fields = ['id', 'name']

class ActivitySerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)
	team = TeamSerializer(read_only=True)
	class Meta:
		model = Activity
		fields = ['id', 'user', 'activity_type', 'duration', 'team']

class WorkoutSerializer(serializers.ModelSerializer):
	class Meta:
		model = Workout
		fields = ['id', 'name', 'description', 'difficulty']

class LeaderboardSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)
	team = TeamSerializer(read_only=True)
	class Meta:
		model = Leaderboard
		fields = ['id', 'user', 'team', 'points']
