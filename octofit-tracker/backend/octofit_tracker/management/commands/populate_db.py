from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        self.stdout.write('Creating teams...')
        
        # Create Teams
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Assemble! The mightiest heroes unite for fitness glory'
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League fitness squad - defending health and wellness'
        )
        
        self.stdout.write(self.style.SUCCESS(f'Created teams: {team_marvel.name}, {team_dc.name}'))
        
        self.stdout.write('Creating users...')
        
        # Create Users - Marvel Heroes
        marvel_users = [
            User.objects.create(
                name='Tony Stark',
                email='ironman@marvel.com',
                password='arc_reactor_3000',
                team_id=str(team_marvel._id)
            ),
            User.objects.create(
                name='Steve Rogers',
                email='captain@marvel.com',
                password='brooklyn_shield',
                team_id=str(team_marvel._id)
            ),
            User.objects.create(
                name='Natasha Romanoff',
                email='blackwidow@marvel.com',
                password='red_room_secret',
                team_id=str(team_marvel._id)
            ),
            User.objects.create(
                name='Thor Odinson',
                email='thor@marvel.com',
                password='mjolnir_worthy',
                team_id=str(team_marvel._id)
            ),
            User.objects.create(
                name='Bruce Banner',
                email='hulk@marvel.com',
                password='gamma_radiation',
                team_id=str(team_marvel._id)
            ),
        ]
        
        # Create Users - DC Heroes
        dc_users = [
            User.objects.create(
                name='Clark Kent',
                email='superman@dc.com',
                password='krypton_son',
                team_id=str(team_dc._id)
            ),
            User.objects.create(
                name='Bruce Wayne',
                email='batman@dc.com',
                password='gotham_knight',
                team_id=str(team_dc._id)
            ),
            User.objects.create(
                name='Diana Prince',
                email='wonderwoman@dc.com',
                password='amazonian_warrior',
                team_id=str(team_dc._id)
            ),
            User.objects.create(
                name='Barry Allen',
                email='flash@dc.com',
                password='speed_force',
                team_id=str(team_dc._id)
            ),
            User.objects.create(
                name='Arthur Curry',
                email='aquaman@dc.com',
                password='atlantis_king',
                team_id=str(team_dc._id)
            ),
        ]
        
        all_users = marvel_users + dc_users
        self.stdout.write(self.style.SUCCESS(f'Created {len(all_users)} users'))
        
        self.stdout.write('Creating activities...')
        
        # Create Activities for Marvel Heroes
        activities_data = [
            # Tony Stark
            {'user': marvel_users[0], 'type': 'Running', 'duration': 45, 'distance': 8.5, 'calories': 650, 'notes': 'Morning run in the new Mark L suit'},
            {'user': marvel_users[0], 'type': 'Strength Training', 'duration': 60, 'distance': None, 'calories': 400, 'notes': 'Testing new repulsor tech'},
            # Steve Rogers
            {'user': marvel_users[1], 'type': 'Running', 'duration': 90, 'distance': 15.0, 'calories': 1200, 'notes': 'Just a light jog around Brooklyn'},
            {'user': marvel_users[1], 'type': 'Boxing', 'duration': 75, 'distance': None, 'calories': 900, 'notes': 'Training with the punching bag'},
            # Natasha Romanoff
            {'user': marvel_users[2], 'type': 'Yoga', 'duration': 60, 'distance': None, 'calories': 300, 'notes': 'Flexibility and balance training'},
            {'user': marvel_users[2], 'type': 'Combat Training', 'duration': 90, 'distance': None, 'calories': 800, 'notes': 'Enhanced martial arts session'},
            # Thor
            {'user': marvel_users[3], 'type': 'Hammer Training', 'duration': 120, 'distance': None, 'calories': 1500, 'notes': 'Mjolnir throwing practice'},
            {'user': marvel_users[3], 'type': 'Running', 'duration': 30, 'distance': 10.0, 'calories': 800, 'notes': 'Lightning speed run'},
            # Bruce Banner
            {'user': marvel_users[4], 'type': 'Swimming', 'duration': 45, 'distance': 2.5, 'calories': 500, 'notes': 'Staying calm in the water'},
            {'user': marvel_users[4], 'type': 'Meditation', 'duration': 30, 'distance': None, 'calories': 100, 'notes': 'Controlling the other guy'},
            
            # DC Heroes
            # Clark Kent
            {'user': dc_users[0], 'type': 'Flying', 'duration': 60, 'distance': 500.0, 'calories': 1800, 'notes': 'Patrol around Metropolis'},
            {'user': dc_users[0], 'type': 'Strength Training', 'duration': 90, 'distance': None, 'calories': 1200, 'notes': 'Lifting with the Fortress equipment'},
            # Bruce Wayne
            {'user': dc_users[1], 'type': 'Combat Training', 'duration': 120, 'distance': None, 'calories': 1100, 'notes': 'Perfecting martial arts techniques'},
            {'user': dc_users[1], 'type': 'Running', 'duration': 60, 'distance': 12.0, 'calories': 850, 'notes': 'Gotham rooftop parkour'},
            # Diana Prince
            {'user': dc_users[2], 'type': 'Sword Training', 'duration': 90, 'distance': None, 'calories': 950, 'notes': 'Amazonian combat drills'},
            {'user': dc_users[2], 'type': 'Running', 'duration': 45, 'distance': 15.0, 'calories': 1000, 'notes': 'Island training regimen'},
            # Barry Allen
            {'user': dc_users[3], 'type': 'Running', 'duration': 15, 'distance': 1000.0, 'calories': 2500, 'notes': 'Just a quick run around the world'},
            {'user': dc_users[3], 'type': 'Speed Training', 'duration': 30, 'distance': 500.0, 'calories': 2000, 'notes': 'Testing top speed limits'},
            # Arthur Curry
            {'user': dc_users[4], 'type': 'Swimming', 'duration': 120, 'distance': 100.0, 'calories': 1600, 'notes': 'Deep sea exploration'},
            {'user': dc_users[4], 'type': 'Strength Training', 'duration': 75, 'distance': None, 'calories': 800, 'notes': 'Underwater weight training'},
        ]
        
        activities = []
        for i, activity_data in enumerate(activities_data):
            activity = Activity.objects.create(
                user_id=str(activity_data['user']._id),
                activity_type=activity_data['type'],
                duration=activity_data['duration'],
                distance=activity_data['distance'],
                calories=activity_data['calories'],
                date=timezone.now() - timedelta(days=i % 7),
                notes=activity_data['notes']
            )
            activities.append(activity)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(activities)} activities'))
        
        self.stdout.write('Creating leaderboard entries...')
        
        # Calculate leaderboard data
        leaderboard_entries = []
        for user in all_users:
            user_activities = Activity.objects.filter(user_id=str(user._id))
            total_calories = sum(a.calories for a in user_activities)
            total_activities = user_activities.count()
            
            leaderboard_entry = Leaderboard.objects.create(
                user_id=str(user._id),
                team_id=user.team_id,
                total_calories=total_calories,
                total_activities=total_activities,
                rank=0
            )
            leaderboard_entries.append((leaderboard_entry, total_calories))
        
        # Assign ranks based on total calories
        leaderboard_entries.sort(key=lambda x: x[1], reverse=True)
        for rank, (entry, _) in enumerate(leaderboard_entries, start=1):
            entry.rank = rank
            entry.save()
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(leaderboard_entries)} leaderboard entries'))
        
        self.stdout.write('Creating workout suggestions...')
        
        # Create Workout suggestions
        workouts = [
            Workout.objects.create(
                name='Super Soldier Bootcamp',
                description='An intense full-body workout inspired by Captain America\'s training regimen',
                category='Strength',
                difficulty='Hard',
                duration=60,
                calories_per_session=700
            ),
            Workout.objects.create(
                name='Web-Slinging Cardio',
                description='High-intensity cardio workout combining agility and endurance',
                category='Cardio',
                difficulty='Medium',
                duration=45,
                calories_per_session=550
            ),
            Workout.objects.create(
                name='Asgardian Thunder Lift',
                description='Heavy strength training with focus on power and explosiveness',
                category='Strength',
                difficulty='Hard',
                duration=75,
                calories_per_session=850
            ),
            Workout.objects.create(
                name='Black Widow Flexibility',
                description='Yoga and stretching routine for improved flexibility and balance',
                category='Flexibility',
                difficulty='Easy',
                duration=30,
                calories_per_session=200
            ),
            Workout.objects.create(
                name='Flash Speed Training',
                description='Sprint intervals and speed work for maximum velocity',
                category='Cardio',
                difficulty='Hard',
                duration=40,
                calories_per_session=800
            ),
            Workout.objects.create(
                name='Atlantean Swim Workout',
                description='Comprehensive swimming workout for endurance and strength',
                category='Swimming',
                difficulty='Medium',
                duration=60,
                calories_per_session=650
            ),
            Workout.objects.create(
                name='Bat-Cave Boxing',
                description='Combat training with focus on striking and defensive techniques',
                category='Combat',
                difficulty='Hard',
                duration=90,
                calories_per_session=950
            ),
            Workout.objects.create(
                name='Kryptonian Core Blast',
                description='Core strengthening exercises for superhuman stability',
                category='Strength',
                difficulty='Medium',
                duration=30,
                calories_per_session=350
            ),
            Workout.objects.create(
                name='Amazonian Warrior Training',
                description='Sword and shield combat drills with bodyweight exercises',
                category='Combat',
                difficulty='Hard',
                duration=75,
                calories_per_session=800
            ),
            Workout.objects.create(
                name='Arc Reactor Recovery',
                description='Light stretching and recovery exercises for active rest days',
                category='Flexibility',
                difficulty='Easy',
                duration=20,
                calories_per_session=150
            ),
        ]
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(workouts)} workout suggestions'))
        
        self.stdout.write(self.style.SUCCESS('Database population completed successfully!'))
        self.stdout.write(f'Summary:')
        self.stdout.write(f'  - Teams: {Team.objects.count()}')
        self.stdout.write(f'  - Users: {User.objects.count()}')
        self.stdout.write(f'  - Activities: {Activity.objects.count()}')
        self.stdout.write(f'  - Leaderboard Entries: {Leaderboard.objects.count()}')
        self.stdout.write(f'  - Workouts: {Workout.objects.count()}')
