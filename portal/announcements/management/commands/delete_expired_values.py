from datetime import datetime, timezone
from django.core.management.base import BaseCommand
from announcements.models import Announcement

class DeleteExpiredAnnouncementsCommand(BaseCommand):
    help = 'Deletes expired announcements and their related images, files and tags'

    def handle(self, *args, **options):
        now = datetime.now(timezone.utc).date()
        expired_announcements = Announcement.objects.filter(date_of_expiring=now)


        for announcement in expired_announcements:
            announcement.delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted announcement with id {announcement.id} and its related images, files and tags.'))