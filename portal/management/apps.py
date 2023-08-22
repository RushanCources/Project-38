import sys
from django.apps import AppConfig


class ProjectadminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'management'

    def ready(self) -> None:
        if 'runserver' not in sys.argv:
            return
        from django.conf import settings
        if settings.DEBUG == True:
            from management.models import User
            user1, created = User.objects.get_or_create(username="aaa1")
            if created:
                user1.first_name="Надежда"
                user1.middle_name="Борисовна"
                user1.last_name="Тукова"
                user1.email="a@a.ru"
                user1.role="Учитель"
                user1.set_password("1")
                user1.save()
            user2, created = User.objects.get_or_create(username="aaa2", first_name="Наталья", middle_name="Львовна",
                                                        last_name="Попова", email="a@a.ru",
                                                        role="Учитель")
            if created:
                user2.last_name="Попова"
                user2.first_name="Наталья"
                user2.middle_name="Львовна"
                user2.email="a@a.ru"
                user2.role="Учитель"
                user2.set_password("1")
                user2.save()
            user3, created = User.objects.get_or_create(username="aaa3")
            if created:
                user3.last_name="Дмитриев"
                user3.first_name="Алексей"
                user3.middle_name="Романович"
                user3.email="a@a.ru"
                user3.role="Ученик"
                user3.set_password("1")
                user3.save()
            user4, created = User.objects.get_or_create(username='d1ffy', last_name='Кокорин', first_name='Петр', middle_name='Алексеевич',
                                                        email='helpersteam96@inbox.ru', role='Администратор')
            if created:
                user4.last_name="Кокорин"
                user4.first_name="Петр"
                user4.middle_name="Алексеевич"
                user4.email="helpersteam96@inbox.ru"
                user4.role="Администратор"
                user4.set_password("1")
                user4.save()
            user5, created = User.objects.get_or_create(username='Cbytl', last_name='Кабанин', first_name='Денис', middle_name='Андреевич',
                                                        email='email@email.ru', role='Администратор')
            if created:
                user5.last_name="Кабанин"
                user5.first_name="Денис"
                user5.middle_name="Андреевич"
                user5.email="email@email.ru"
                user5.role="Администратор"
                user5.set_password("555555")
                user5.save()
        return super().ready()
        