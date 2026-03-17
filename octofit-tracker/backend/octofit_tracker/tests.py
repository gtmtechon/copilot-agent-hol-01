from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Activity
from .models import Leaderboard
from .models import Team
from .models import User
from .models import Workout


class OctofitApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.marvel = Team.objects.create(name='Marvel Team', universe='marvel')
        self.user = User.objects.create(
            name='Iron Man',
            email='ironman@test.dev',
            team=self.marvel,
        )
        Activity.objects.create(
            user=self.user,
            activity_type='Running',
            duration_minutes=40,
            calories_burned=500,
        )
        Leaderboard.objects.create(user=self.user, score=999, rank=1)
        Workout.objects.create(
            user=self.user,
            title='Arc Reactor Cardio',
            description='Intervals',
            intensity='high',
        )

    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)

    def test_collection_endpoints(self):
        endpoints = [
            '/api/users/',
            '/api/teams/',
            '/api/activities/',
            '/api/leaderboard/',
            '/api/workouts/',
        ]

        for endpoint in endpoints:
            response = self.client.get(endpoint)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertGreaterEqual(len(response.data), 1)
