from django.db import models
from django.db.models import FileField

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
        if subject in ["Математика", "Алгебра", "Геометрия", "Теория вероятностей и статистика", "Информатика",
                       "География", "Биология", "Физика",
                       "Химия", "Основы безопасности жизнедеятельности", "Естествознание", "Экология", "Астрономия",
                       "История", "Обществознание",
                       "Экономика", "Право", "Разговоры о важном", "Краеведение",
                       "Основы религиозных культур и светской этики", "Родная литература",
                       "Русский язык", "Литература", "Иностранный язык(Английский)", "Иностранный язык(Французский)",
                       "Иностранный язык(Немецкий)",
                       "Труд", "Технология", "Черчение", "Индивидуальный проект", "Физическая культура", "Музыка",
                       "Изобразительное искусство",
                       "Другая научная область/предмет"]:
            self._subject = subject

    def get_subject(self):
        return self._subject

    def set_status(self, n):
        if n in self._statuses:
            self._status = n
            self.save()

    def get_status(self):
        return self._status


MAX_FILE_VERSION = 3


class File(models.Model):
    project = models.ForeignKey(Project, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='project_files', blank=True, null=True)
    version = models.IntegerField(default=1)
    previous_file = models.ForeignKey('File', related_name="previous", null=True, on_delete=models.SET_NULL)

    def update_file(self):
        if self.version == MAX_FILE_VERSION:
            self.delete()
        elif self.previous_file is not None:
            self.previous_file.update_file()
            self.file = self.previous_file.file
            self.version += 1
            self.save()
