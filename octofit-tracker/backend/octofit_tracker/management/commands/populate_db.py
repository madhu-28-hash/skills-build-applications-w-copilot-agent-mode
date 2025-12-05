from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel', is_superhero=True)
        captain = User.objects.create(email='captain@marvel.com', name='Captain America', team='marvel', is_superhero=True)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='dc', is_superhero=True)
        superman = User.objects.create(email='superman@dc.com', name='Superman', team='dc', is_superhero=True)

        # Activities
        Activity.objects.create(user='Iron Man', activity_type='run', duration=30, date='2025-12-01')
        Activity.objects.create(user='Captain America', activity_type='cycle', duration=45, date='2025-12-02')
        Activity.objects.create(user='Batman', activity_type='swim', duration=60, date='2025-12-03')
        Activity.objects.create(user='Superman', activity_type='fly', duration=120, date='2025-12-04')

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=75)
        Leaderboard.objects.create(team='dc', points=180)

        # Workouts
        Workout.objects.create(name='Pushups', description='Upper body strength', difficulty='easy')
        Workout.objects.create(name='Sprints', description='Speed training', difficulty='medium')
        Workout.objects.create(name='Flight', description='Aerial endurance', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
