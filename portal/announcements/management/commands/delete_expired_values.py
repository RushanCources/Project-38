from datetime import datetime, timezone
from django.core.management.base import BaseCommand
from announcements.models import Announcement


class Command(BaseCommand):
    help = 'Deletes expired announcements and their related images and files'

    def handle(self, *args, **options):
        now = datetime.now(timezone.utc)
        announcements = Announcement.objects.all()

        for announcement in announcements:
            if announcement.date_of_expiring <= now:

                files = announcement.files.all()

                for file in files:
                    file.file.delete()
                    file.delete()

                self.stdout.write(self.style.SUCCESS(f'Successfully deleted announcement with id {announcement.id} and its related image and files.'))
                announcement.delete()
