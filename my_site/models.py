from django.db import models

# Create your models here.
class student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)

    def _str_(self):
        return self.first_name


