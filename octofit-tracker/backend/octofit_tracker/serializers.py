from rest_framework import serializers

from .models import Activity
from .models import Leaderboard
from .models import Team
from .models import User
from .models import Workout


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Team
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    team_name = serializers.CharField(source='team.name', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'team', 'team_name']


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user_name = serializers.CharField(source='user.name', read_only=True)

    class Meta:
        model = Activity
        fields = [
            'id',
            'user',
            'user_name',
            'activity_type',
            'duration_minutes',
            'calories_burned',
        ]


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user_name = serializers.CharField(source='user.name', read_only=True)

    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'user_name', 'score', 'rank']


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user_name = serializers.CharField(source='user.name', read_only=True)

    class Meta:
        model = Workout
        fields = ['id', 'user', 'user_name', 'title', 'description', 'intensity']
