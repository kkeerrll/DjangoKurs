from django.db import models

# Create your models here.


class Mailing(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    audience = models.CharField(max_length=50)

class Client(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.email


class Mailing(models.Model):
    TIME_CHOICES = [
        ('08:00', '08:00'),
        ('09:00', '09:00'),
        ('10:00', '10:00'),
        # Добавьте другие варианты времени
    ]

    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    time = models.CharField(max_length=5, choices=TIME_CHOICES)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    status = models.CharField(max_length=10)
    message = models.ForeignKey('Message', on_delete=models.CASCADE)

    def __str__(self):
        return f"Mailing - {self.id}"


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.subject


class Log(models.Model):
    mailing = models.ForeignKey('Mailing', on_delete=models.CASCADE)
    message = models.ForeignKey('Message', on_delete=models.CASCADE)
    recipient = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    response = models.TextField()

    def __str__(self):
        return f"Log - {self.id}"



