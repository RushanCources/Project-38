# import sqlite3
# from datetime import date, datetime
#
# conn = sqlite3.connect(r"/home/a/lycprojkect/Project-38/portal/db.sqlite3")
# cur = conn.cursor()
# cur.execute("SELECT date_of_expiring FROM announcements_announcement")
# dates = cur.fetchall()
#
# for i in dates:
#     if datetime.now().date() >= date.fromisoformat(i[0][:10]):
#         cur.execute("DELETE FROM announcements_announcement WHERE date_of_expiring=?", (i[0],))
#
# conn.commit()
# conn.close()

from datetime import datetime, timezone
from django.core.management.base import BaseCommand
from announcements.models import Announcement

class DeleteExpiredAnnouncementsCommand(BaseCommand):
    help = 'Deletes expired announcements and their related images and tags'

    def handle(self, *args, **options):
        now = datetime.now(timezone.utc).date()
        expired_announcements = Announcement.objects.filter(date_of_expiring=now)
        for announcement in expired_announcements:
            announcement.delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted announcement with id {announcement.id} and its related images and tags.'))