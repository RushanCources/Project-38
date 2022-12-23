from django.db import models
from management.models import Teacher, Student

class Project(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE())
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE())
    name = models.CharField(max_length=30)
    __statuses = ["on work", "send to verification", "done"]
    __status = models.CharField(max_length=30)
    def setStatus(self, n):
        if n in self.__statuses:
            self.status = n
    def getStatus(self):
        return self.status

class Request(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE())
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE())
