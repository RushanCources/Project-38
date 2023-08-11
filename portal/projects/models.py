import os

from django.db import models
from django.db.models import FileField
from django.dispatch import receiver

from management.models import User


class Project(models.Model):
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="students")
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="teachers")
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000, null=True)
    _statuses = ["send request", "on work", "send to verification", "done"]
    _status = models.CharField(max_length=30)
    _subject = models.CharField(max_length=20, null=True)

    # фильтрация предметов при записи их в бд(что бы не удалось поставить не существующий предмет
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

    # фильтрация статусов при установке их в бд
    def set_status(self, n):
        if n in self._statuses:
            self._status = n
            self.save()

    def get_status(self):
        return self._status


# эта константа показывает сколько версий может быть у одного файла
MAX_FILE_VERSION = 3


class File(models.Model):
    project: Project = models.ForeignKey(Project, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to=f'project_files', blank=True, null=True)
    version = models.IntegerField(default=1)
    previous_file: 'File' = models.ForeignKey('File', related_name="previous", null=True, on_delete=models.SET_NULL)
    comment = models.CharField(max_length=1024, null=True)

    # оновление файла
    def update_file(self, file=None):
        if self.version == MAX_FILE_VERSION:
            self.delete()
        elif self.version == 1 and file is not None:
            new_obj = File.objects.create(project=self.project, file=file, version=1, previous_file=self)
            new_obj.save()
            self.version += 1
            self.save()
        else:  # если файл находится не в начале и не в конце по версиям
            self.version += 1
            self.save()
        if self.previous_file is not None:
            self.previous_file.update_file()

    # отправление файла в корзину
    def move_to_trash(self):
        if self.version == 1:
            self.version = -1
        self.save()

    # восстановление файла из корзины
    def restore(self):
        self.version = 1
        self.save()


# Удаление всех предыдущих файлов
@receiver(models.signals.pre_delete, sender=File)
def delete_file(sender, instance: File, *args, **kwargs):
    if instance.previous_file is not None:
        instance.previous_file.delete()
