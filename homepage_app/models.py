from django.db import models

class Yozuvchilar(models.Model):
    STATUS_CHOICES = [
        ('W','Writer'),
        ('P','Poet'),
        ('U','User'),
    ]
    fullname = models.CharField(max_length=50)
    about = models.TextField(max_length=100)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.fullname

