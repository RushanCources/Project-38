from django.db import models
from management.models import User

class Project(models.Model):
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="students")
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="teachers")
    name = models.CharField(max_length=30)
    _statuses = ["send request", "on work", "send to verification", "done"]
    _status = models.CharField(max_length=30)
    def setStatus(self, n):
        if n in self._statuses:
            self._status = n
            self.save()
    def getStatus(self):
        return self.status

