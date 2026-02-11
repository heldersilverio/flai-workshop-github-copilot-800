from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['_id', 'name', 'email', 'password', 'team_id', 'created_at']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user


class TeamSerializer(serializers.ModelSerializer):
    member_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Team
        fields = ['_id', 'name', 'description', 'created_at', 'member_count']
    
    def get_member_count(self, obj):
        return User.objects.filter(team_id=str(obj._id)).count()


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['_id', 'user_id', 'activity_type', 'duration', 'distance', 'calories', 'date', 'notes']


class LeaderboardSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    team_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Leaderboard
        fields = ['_id', 'user_id', 'team_id', 'user_name', 'team_name', 'total_calories', 'total_activities', 'rank', 'updated_at']
    
    def get_user_name(self, obj):
        try:
            user = User.objects.get(_id=obj.user_id)
            return user.name
        except User.DoesNotExist:
            return 'Unknown User'
    
    def get_team_name(self, obj):
        try:
            team = Team.objects.get(_id=obj.team_id)
            return team.name
        except Team.DoesNotExist:
            return 'No Team'


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description', 'category', 'difficulty', 'duration', 'calories_per_session']
