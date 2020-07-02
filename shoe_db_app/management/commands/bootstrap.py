from django.core.management.base import BaseCommand, CommandError
from shoe_db_app.models import ShoeType, ShoeColor

class Command(BaseCommand):
    def add_arguments(self, parser):
        # boot_type determines which attribute gets updated
        parser.add_argument('--boot_type', type=str)
        parser.add_argument('data',nargs='+', type=str)
    
    def handle(self, *args, **options):
        if options['boot_type'] == 'shoetype':
            for i in options['data']:
                print(i)
                obs = ShoeType(style=i)
                obs.save()
        if options['boot_type'] == 'shoecolor':
            for i in options['data']:
                obs = ShoeColor(color_name=i)
                obs.save()
