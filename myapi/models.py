from django.db import models

class Package(models.Model):
    application = models.CharField(max_length = 100)
    package_name = models.CharField(max_length = 100)
    package_version_code = models.CharField(max_length = 100)
