from django.contrib import admin

from .models import Activity
from .models import Leaderboard
from .models import Team
from .models import User
from .models import Workout


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'universe')
    search_fields = ('name', 'universe')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'team')
    search_fields = ('name', 'email')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'duration_minutes', 'calories_burned')
    search_fields = ('user__name', 'activity_type')


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'rank')
    search_fields = ('user__name',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'intensity')
    search_fields = ('user__name', 'title', 'intensity')
