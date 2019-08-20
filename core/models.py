from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app_details', args=[str(self.id)])


class Key(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(Application, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    token = models.CharField(max_length=64)
    hwid = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)
    activations = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    disable_at = models.DateTimeField(blank=True, null=True)
    last_activation = models.DateTimeField(blank=True, null=True)
    last_check = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"App: {self.app.name} Token: {self.token}"

    def get_absolute_url(self):
        return reverse('key_details', args=[str(self.id)])


class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(Application, on_delete=models.CASCADE)
    key = models.ForeignKey(Key, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    event = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.event}: {self.description}"
