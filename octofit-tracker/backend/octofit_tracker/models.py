from bson import ObjectId
from djongo import models


class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100, unique=True)
    universe = models.CharField(max_length=20)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name


class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField()

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f"{self.user} - {self.activity_type}"


class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    rank = models.PositiveIntegerField()

    class Meta:
        db_table = 'leaderboard'

    def __str__(self):
        return f"{self.user} - rank {self.rank}"


class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    intensity = models.CharField(max_length=30)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return f"{self.user} - {self.title}"
