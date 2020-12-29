from django.db import models

# Create your models here.


class Teammates(models.Model):
    title = models.CharField('Ф.И.О', max_length=40)
    DOB = models.DateField('дата рождения')
    Expirience = models.DateField('стаж', help_text='дата начала занятий')
    Duration = models.DurationField()
    Email = models.EmailField('Email')

    def __str__(self):
        return self.title

