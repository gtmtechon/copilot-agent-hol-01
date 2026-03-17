from rest_framework import viewsets

from .models import Activity
from .models import Leaderboard
from .models import Team
from .models import User
from .models import Workout
from .serializers import ActivitySerializer
from .serializers import LeaderboardSerializer
from .serializers import TeamSerializer
from .serializers import UserSerializer
from .serializers import WorkoutSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('activity_type')
    serializer_class = ActivitySerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all().order_by('rank')
    serializer_class = LeaderboardSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all().order_by('title')
    serializer_class = WorkoutSerializer
