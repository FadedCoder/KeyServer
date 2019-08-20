from django.contrib import admin
from . import models


admin.site.register(models.Application)
admin.site.register(models.Key)
admin.site.register(models.AuditLog)
