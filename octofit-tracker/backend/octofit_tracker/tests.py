from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime


class UserModelTest(TestCase):
    """Test User model"""
    
    def setUp(self):
        self.user = User.objects.create(
            name="Test User",
            email="test@example.com",
            password="testpass123"
        )
    
    def test_user_creation(self):
        """Test user is created successfully"""
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertIsNotNone(self.user._id)


class TeamModelTest(TestCase):
    """Test Team model"""
    
    def setUp(self):
        self.team = Team.objects.create(
            name="Test Team",
            description="A test team"
        )
    
    def test_team_creation(self):
        """Test team is created successfully"""
        self.assertEqual(self.team.name, "Test Team")
        self.assertEqual(self.team.description, "A test team")
        self.assertIsNotNone(self.team._id)


class ActivityModelTest(TestCase):
    """Test Activity model"""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            user_id="user123",
            activity_type="Running",
            duration=30,
            distance=5.0,
            calories=300,
            date=datetime.now()
        )
    
    def test_activity_creation(self):
        """Test activity is created successfully"""
        self.assertEqual(self.activity.activity_type, "Running")
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories, 300)
        self.assertIsNotNone(self.activity._id)


class LeaderboardModelTest(TestCase):
    """Test Leaderboard model"""
    
    def setUp(self):
        self.leaderboard = Leaderboard.objects.create(
            user_id="user123",
            team_id="team456",
            total_calories=1000,
            total_activities=10,
            rank=1
        )
    
    def test_leaderboard_creation(self):
        """Test leaderboard entry is created successfully"""
        self.assertEqual(self.leaderboard.user_id, "user123")
        self.assertEqual(self.leaderboard.total_calories, 1000)
        self.assertEqual(self.leaderboard.rank, 1)
        self.assertIsNotNone(self.leaderboard._id)


class WorkoutModelTest(TestCase):
    """Test Workout model"""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            name="Morning Run",
            description="A refreshing morning run",
            category="Cardio",
            difficulty="Medium",
            duration=45,
            calories_per_session=400
        )
    
    def test_workout_creation(self):
        """Test workout is created successfully"""
        self.assertEqual(self.workout.name, "Morning Run")
        self.assertEqual(self.workout.category, "Cardio")
        self.assertEqual(self.workout.difficulty, "Medium")
        self.assertIsNotNone(self.workout._id)


class APITestCases(APITestCase):
    """Test API endpoints"""
    
    def setUp(self):
        self.client = APIClient()
    
    def test_api_root(self):
        """Test API root endpoint"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
    
    def test_users_endpoint(self):
        """Test users endpoint"""
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_teams_endpoint(self):
        """Test teams endpoint"""
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_activities_endpoint(self):
        """Test activities endpoint"""
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_leaderboard_endpoint(self):
        """Test leaderboard endpoint"""
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_workouts_endpoint(self):
        """Test workouts endpoint"""
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
