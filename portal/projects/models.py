from django.db import models
from management.models import User

class Project(models.Model):
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="students")
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="teachers")
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000, null=True)
    _statuses = ["send request", "on work", "send to verification", "done"]
    _status = models.CharField(max_length=30)
    _subject = models.CharField(max_length=20, null=True)

    def set_subject(self, subject):
        if subject in ["Математика", "Алгебра", "Геометрия", "Теория вероятностей и статистика", "Информатика", "География", "Биология", "Физика",
                       "Химия", "Основы безопасности жизнедеятельности", "Естествознание", "Экология", "Астрономия", "История", "Обществознание",
                       "Экономика", "Право", "Разговоры о важном", "Краеведение", "Основы религиозных культур и светской этики", "Родная литература",
                       "Русский язык", "Литература", "Иностранный язык(Английский)", "Иностранный язык(Французский)", "Иностранный язык(Немецкий)",
                       "Труд", "Технология", "Черчение", "Индивидуальный проект", "Физическая культура", "Музыка", "Изобразительное искусство",
                       "Другая научная область/предмет"]:
            self._subject = subject

    def get_subject(self):
        return self._subject


    def setStatus(self, n):
        if n in self._statuses:
            self._status = n
            self.save()


    def getStatus(self):
        return self._status

