from django.core.management.base import BaseCommand

from octofit_tracker.models import Activity
from octofit_tracker.models import Leaderboard
from octofit_tracker.models import Team
from octofit_tracker.models import User
from octofit_tracker.models import Workout


class Command(BaseCommand):
    help = 'octofit_db 데이터베이스에 테스트 데이터를 입력합니다.'

    def handle(self, *args, **options):
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        marvel = Team.objects.create(name='Marvel Team', universe='marvel')
        dc = Team.objects.create(name='DC Team', universe='dc')

        users = [
            User.objects.create(name='Iron Man', email='ironman@octofit.dev', team=marvel),
            User.objects.create(name='Captain America', email='captain@octofit.dev', team=marvel),
            User.objects.create(name='Batman', email='batman@octofit.dev', team=dc),
            User.objects.create(name='Wonder Woman', email='wonderwoman@octofit.dev', team=dc),
        ]

        activity_samples = [
            ('Running', 45, 520),
            ('Cycling', 35, 410),
            ('HIIT', 30, 460),
            ('Strength Training', 50, 600),
        ]

        workout_samples = [
            ('Arc Reactor Cardio', 'Intervals and sprint sessions.', 'high'),
            ('Shield Endurance', 'Core and long-distance conditioning.', 'medium'),
            ('Gotham Strength', 'Compound lifts and bodyweight drills.', 'high'),
            ('Amazon Agility', 'Mobility and agility circuit.', 'medium'),
        ]

        scores = [980, 910, 940, 920]

        for idx, user in enumerate(users):
            activity_type, duration, calories = activity_samples[idx]
            title, description, intensity = workout_samples[idx]
            Activity.objects.create(
                user=user,
                activity_type=activity_type,
                duration_minutes=duration,
                calories_burned=calories,
            )
            Workout.objects.create(
                user=user,
                title=title,
                description=description,
                intensity=intensity,
            )

        ranked = sorted(zip(users, scores), key=lambda x: x[1], reverse=True)
        for rank, (user, score) in enumerate(ranked, start=1):
            Leaderboard.objects.create(user=user, score=score, rank=rank)

        self.stdout.write(self.style.SUCCESS('테스트 데이터 입력 완료'))
