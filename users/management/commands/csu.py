from django.conf import settings
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = 'Удалить всех пользователей и группы, создать суперюзера и группу менджер'

    def handle(self, *args, **kwargs):
        Group.objects.all().delete()
        User.objects.all().delete()
        user = User.objects.create(
            email='kazan313131@gmail.com',
            first_name='Admin',
            last_name='MailingCenter',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        user.set_password('140386Odd')
        user.save()
