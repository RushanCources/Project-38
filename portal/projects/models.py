import os
from django.db.models import FileField, CharField, SET_NULL, ForeignKey, Model, IntegerField, CASCADE
from django.db.models.signals import pre_delete, pre_save, pre_init, post_init
from django.dispatch import receiver

from management.models import User
from projects.FileStorage import MyStorage


class Project(Model):
    student = ForeignKey(User, on_delete=SET_NULL, null=True, related_name="students")
    teacher = ForeignKey(User, on_delete=SET_NULL, null=True, related_name="teachers")
    name = CharField(max_length=30)
    description = CharField(max_length=1000, null=True)
    _statuses = ["send request", "on work", "send to verification", "done"]
    _status = CharField(max_length=30)
    _subjects = CharField(max_length=100, null=True)
    _types = ['Проект', 'НОУ']
    _type = CharField(max_length=10, null=True)
    problem = CharField(max_length=1000, null=True)
    relevance = CharField(max_length=1000, null=True)
    target = CharField(max_length=1000, null=True)
    tasks = CharField(max_length=1000, null=True)
    expected_results = CharField(max_length=1000, null=True)

    # фильтрация предметов при записи их в бд(что бы не удалось поставить не существующий предмет
    def set_subject(self, subjects: str):
        flag = True
        for subject in subjects.split(','):
            if subject not in ["Математика", "Алгебра", "Геометрия", "Теория вероятностей и статистика", "Информатика",
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
                flag = False
        if flag:
            self._subjects = subjects
            self.save()

    def get_subjects(self):
        return self._subjects

    # фильтрация статусов при установке их в бд
    def set_status(self, n):
        if n in self._statuses:
            self._status = n
            self.save()

    def get_status(self):
        return self._status

    def set_type(self, project_type):
        if project_type in self._types:
            self._type = project_type
            self.save()

    def get_type(self):
        return self._type


# эта константа показывает сколько версий может быть у одного файла
MAX_FILE_VERSION = 3


def get_upload_path(instance, filename):
    return f'project_files/{instance.project.id}/{filename}'

def get_file_name(instance, *args):
    return os.path.split(instance.file)[1]

class File(Model):
    _tag = CharField(max_length=20, null=True)
    _tags = ['Реферат', 'Презентация', 'Защита', 'Другое']
    project: Project = ForeignKey(Project, related_name='files', on_delete=CASCADE)
    file = FileField(upload_to=get_upload_path, blank=True, null=True, storage=MyStorage)
    version = IntegerField(default=1)
    previous_file: 'File' = ForeignKey('File', related_name="previous", null=True, on_delete=SET_NULL)
    comment = CharField(max_length=1024, null=True)
    name = CharField(max_length=100, null=True)

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

    def set_tag(self, tag):
        if tag in self._tags:
            self._tag = tag
            self.save()
    
    def get_prevent_files(self):
        previous_file = self.previous_file
        previous_files = []
        while previous_file is not None:  # Запуск цикла, пока у предыдущего файла есть предыдущий файл
            previous_files.append(previous_file)
            previous_file: File = previous_file.previous_file
        return previous_files


# Удаление всех предыдущих файлов
@receiver(pre_delete, sender=File)
def delete_file(sender, instance: File, *args, **kwargs):
    if instance.previous_file is not None:
        instance.previous_file.delete()

@receiver(post_init, sender=File)
def set_name(sender, instance, **kwargs):
    instance.name = os.path.split(instance.file.name)[1]
