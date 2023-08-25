import sys
from django.apps import AppConfig



class ProjectlistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'subjects'

    def ready(self) -> None:
        if 'runserver' not in sys.argv:
            return
        from .models import Subject
        subjects_names  = ["Математика", "Алгебра", "Геометрия", "Теория вероятностей и статистика", "Информатика",
                           "География", "Биология", "Физика",
                           "Химия", "Основы безопасности жизнедеятельности", "Естествознание", "Экология", "Астрономия",
                           "История", "Обществознание",
                           "Экономика", "Право", "Разговоры о важном", "Краеведение",
                           "Основы религиозных культур и светской этики", "Родная литература",
                           "Русский язык", "Литература", "Иностранный язык(Английский)", "Иностранный язык(Французский)",
                           "Иностранный язык(Немецкий)",
                           "Труд", "Технология", "Черчение", "Индивидуальный проект", "Физическая культура", "Музыка",
                           "Изобразительное искусство",
                           "Другая научная область/предмет"]
        for subject_name in subjects_names:
            subject, cteated=Subject.objects.get_or_create(name=subject_name)
