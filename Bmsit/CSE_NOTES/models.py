from django.db import models


# Create your models here.
class cnscl(models.Model):
    qno = models.PositiveIntegerField()
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
