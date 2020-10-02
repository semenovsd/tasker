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

    # def save(self, *args, **kwargs):
    #     """
    #     This method override parent class’ methods for Task model
    #     and write log any time when Task saved.
    #     """
    #     super().save(*args, **kwargs)
    #     log = Log(
    #         title=self.title,
    #         description=self.description,
    #         status=self.status,
    #         end_date=self.end_date,
    #         user=self.user,  # user_id
    #     )
    #     log.save()
    #     print(log.__dict__)


class Log(models.Model):
    id = models.IntegerField(verbose_name='Log ID', primary_key=True, db_index=True, unique=True, auto_created=True)
    task_id = models.ForeignKey(Task, verbose_name='Title', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Title', unique=True, max_length=64)
    description = models.CharField(verbose_name='Description', max_length=256, blank=True)
    status = models.CharField(verbose_name='Status', max_length=9)
    end_date = models.DateField(verbose_name='End date')
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)


# from django.db.models.signals import post_save
# # https://docs.djangoproject.com/en/3.1/ref/signals/#django.db.models.signals.post_save
#
#
# def task_logger(instance, **kwargs):
#     """
#     Write log any time when Task saved.
#     """
#     log = Log(
#         title=instance.title,
#         description=instance.description,
#         status=instance.status,
#         end_date=instance.end_date,
#         user=instance.user,
#     )
#     log.save()
#     print(f'\n\n\n{instance.__dict__}\n\n\n')
#
#
# post_save.connect(task_logger, sender=Task)
