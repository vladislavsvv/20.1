from django.core.management import BaseCommand, call_command
from django.conf import settings
from django.db import ProgrammingError, IntegrityError


class Command(BaseCommand):
    requires_migrations_checks = True

    def handle(self, *args, **options):
        path = settings.BASE_DIR.joinpath('posts.json')

        try:
            call_command('loaddata', path)
        except ProgrammingError:
            pass
        except IntegrityError as e:
            self.stdout.write(f'Invalid fixtures: {e}', self.style.NOTICE)
        else:
            self.stdout.write(
                'Blog fixtures have been loaded',
                self.style.SUCCESS
            )
