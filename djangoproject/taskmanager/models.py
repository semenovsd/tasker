from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class Task(models.Model):
    STATE = [
        ('New', 'Новая'),
        ('Scheduled', 'Запланированная'),
        ('InWork', 'Работе'),
        ('Completed', 'Завершённая'),
    ]

    id = models.IntegerField(verbose_name='Task ID', primary_key=True, db_index=True, unique=True, auto_created=True)
    title = models.CharField(verbose_name='Title', unique=True, max_length=64)
    description = models.CharField(verbose_name='Description', max_length=256, blank=True)
    date = models.DateTimeField(verbose_name='Create date', auto_now_add=True)
    status = models.CharField(verbose_name='Status', max_length=9, choices=STATE)
    end_date = models.DateField(verbose_name='End date')
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

# class Log(models.Model):
#
