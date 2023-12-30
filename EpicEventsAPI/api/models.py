from django.db import models
from django.conf import settings


class Client(models.Model):

    information = models.CharField(max_length=50)
    name = models.fields.CharField(max_length=50)
    email = models.EmailField()
    telephone = models.CharField(max_length=13)
    compagny_name = models.CharField(max_length=50)
    last_update = models.DateField()
    creation_date = models.DateField()

    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='client_support_contacts')


class Contract(models.Model):

    class Status(models.TextChoices):
        SIGN = "Sign"
        TO_SIGN = "To-sign"

    total_amount = models.fields.FloatField()
    remaining_amount = models.fields.FloatField()
    status = models.fields.CharField(choices=Status.choices, max_length=10)
    creation_date = models.DateField()

    client = models.ForeignKey(
        to=Client, on_delete=models.CASCADE,
        related_name='contracts')
    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='contract_support_contacts')


class Event(models.Model):
    title = models.CharField(max_length=50)
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)

    date_start = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_end = models.DateTimeField(auto_now=False, auto_now_add=False)
    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='event_support_contacts')
