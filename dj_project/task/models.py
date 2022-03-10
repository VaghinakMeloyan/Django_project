from django.db import models
from django.contrib.auth.models import User
from .choices import STATUS_CHOICE

class Task(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICE, default=0)

    def __str__(self):
        return f"{self.name}--{self.created_at}"























#
# class Task(models.Model):
#     STATUS_CHOICES = (
#         (1, "new"),
#         (2, "doing"),
#         (3, "done"),
#     )
#
#     name = models.CharField(max_length=50)
#     description = models.TextField()
#     status = models.IntegerField(choices=STATUS_CHOICES)
#     created_at = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.name}-- {self.creatid_at}"