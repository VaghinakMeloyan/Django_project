from django.db import models

class Task(models.Model):
    STATUS_CHOICES = (
        (0, "new"),
        (1, "doing"),
        (2, "done"),
    )

    name = models.CharField(max_length=30)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return f"{self.name}---{self.created_at}"

class Target(models.Model):
    STATUS_CHOICE = (
        (0, "new"),
        (1, "doing"),
        (2, "done")
    )

    name = models.CharField(max_length=40)
    description = models.TextField("Learning Python")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICE, default=2)

    def __str__(self):
        return f"{self.name}"