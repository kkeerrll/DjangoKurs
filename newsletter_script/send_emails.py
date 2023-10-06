import datetime
import smtplib

import data
import schedule
import time

from django.contrib.sites import requests
from django.template.defaulttags import url


def send_email(recipient, subject, message):
    # Отправка письма
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        print(f"Email successfully sent to {recipient}")
    except requests.exceptions.RequestException as e:
        # Обработка ошибок запроса к внешнему сервису (например, проблемы с соединением, ошибки HTTP)
        print(f"An error occurred while sending the email to {recipient}: {e}")
    except Exception as e:
        # Обработка других ошибок, возникающих в процессе отправки
        print(f"An unexpected error occurred while sending the email to {recipient}: {e}")

    # Добавить задержку перед повторной попыткой, если требуется
    time.sleep(1)



# Отправка email

def send_emails():
    recipients = {
        'recipient1@example.com': 'Recipient 1',
        'recipient2@example.com': 'Recipient 2',
        'recipient3@example.com': 'Recipient 3',
        # Другие клиенты из справочника
    }

    current_time = datetime.datetime.now().time()

    active_mailings = Mailing.objects.filter(start_time__lte=current_time, end_time__gte=current_time, status='active')

    for mailing in active_mailings:
        recipients_emails = mailing.client_set.values_list('email', flat=True)

        for recipient_email in recipients_emails:
            recipient_name = recipients.get(recipient_email, 'Unknown')
            send_email(recipient_email, mailing.subject, mailing.body)

            log = Log(mailing=mailing, recipient=recipient_email, timestamp=datetime.datetime.now(), status='sent',
                      response='Success')
            log.save()


# Поиск рассылок, которые должны быть запущены в будущем и установка расписания для автоматического запуска по наступлению времени старта
future_mailings = Mailing.objects.filter(start_time__gt=datetime.datetime.now().time())
for mailing in future_mailings:
    schedule.every().day.at(mailing.start_time.strftime('%H:%M')).do(send_emails, mailing=mailing)

while True:
    schedule.run_pending()
    time.sleep(1)
