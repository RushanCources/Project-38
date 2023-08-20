from django.apps import AppConfig
import sys

class projectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projects'

    def ready(self) -> None:
        if 'runserver' not in sys.argv:
            return
        from django.conf import settings
        if settings.DEBUG == True:
            from management.models import User
            from projects.models import Project
            project1, created = Project.objects.get_or_create(id=1)
            if created:
                project1.name = 'LK-99, сверхпроводимость'
                project1.description = 'Открытие и тестирование нового материала на наличие свойств сверхпроводимости'
                project1.teacher = User.objects.get(username='aaa1')
                project1.student = User.objects.get(username='aaa3')
                project1.set_subject('Физика')
                project1.set_status("send request")
                project1.save()
        return super().ready()
