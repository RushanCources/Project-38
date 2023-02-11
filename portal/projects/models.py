from django.db import models
from management.models import Teacher, Student

class Project(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30)
    _statuses = ["send request", "on work", "send to verification", "done"]
    _status = models.CharField(max_length=30)
    def setStatus(self, n):
        if n in self._statuses:
            self.status = n
    def getStatus(self):
        return self.status

