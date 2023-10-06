from django.db import models

# Create your models here.


class Mailing(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    audience = models.CharField(max_length=50)


# class Client(models.Model):
#     email = models.CharField(max_length=50, blank=False, verbose_name='email')
#     name = models.TextField(verbose_name='ФИО', blank=False)
#     comment = models.TextField(verbose_name='комментарий', blank=False)

    # def __str__(self):
    #     return f'{self.name}, {self.description}'

    # class Meta:
    #     ordering = ('name',)
    #     verbose_name = 'Категория'
    #     verbose_name_plural = 'Категории'

# class Mail(models.Model):
#     id = models.IntegerField()
#     header = models.TextField(verbose_name='тема')
#     body = models.CharField(max_length=50, blank=False, verbose_name='тело')
#
# class Settings(models.Model):
#     mail_id = models.ForeignKey(Mail, on_delete=models.CASCADE, default=1, verbose_name='id')
#     time = models.DateTimeField(auto_now_add=True)
#     frequency = models.TextField(verbose_name='периодичность')
#     status = models.CharField(max_length=50, blank=False, verbose_name='статус рассылки')
#
#
# class Log(models.Model):
#     mail_id = models.ForeignKey(Mail, on_delete=models.CASCADE, default=1, verbose_name='id')
#     time = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=50, blank=False, verbose_name='статус попытки')
#     response = models.IntegerField()
