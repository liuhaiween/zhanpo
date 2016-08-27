from django.contrib import admin

# Register your models here.
import models
admin.site.register(models.zuser)
admin.site.register(models.zgroup)
admin.site.register(models.zdpmt)
admin.site.register(models.zblacklist)