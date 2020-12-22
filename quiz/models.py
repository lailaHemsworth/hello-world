from django.db import models
class question(models.Model):
    objects = models.Manager

    text = models.CharField(max_length=50)
    complete = models.BooleanField(default = False)
    def __str__(self):
        return self.text

