from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    identification = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    role = models.CharField(max_length=15)
    tel1 = models.CharField(max_length=50, null=True, blank=True)
    tel2 = models.CharField(max_length=50, null=True, blank=True)
    cc_email = models.CharField(max_length=50, null=True, blank=True)
    jobPosition = models.CharField(max_length=50, null=True, blank=True)
    birthDate = models.DateTimeField(null=True, blank=True)
    state = models.CharField(max_length=15)

class Category(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=15)

class Subcategory(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=15)

class TicketType(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=15)

class TicketState(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=15)

class Ticket(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, null=True, blank=True, on_delete=models.CASCADE)
    ticketType = models.ForeignKey(TicketType, null=True, blank=True, on_delete=models.CASCADE)
    ticketState = models.ForeignKey(TicketState, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    desc = models.TextField(null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    docDate = models.DateTimeField(auto_now=True, null=True, blank=True)
    dueDate = models.DateTimeField(null=True, blank=True)
    closeDate = models.DateTimeField(null=True, blank=True)
    weight = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    follow = models.TextField(null=True, blank=True)
    solution = models.TextField(null=True, blank=True)
    isDeleted = models.CharField(max_length=1)


class TicketActivity(models.Model):
    ticket = models.ForeignKey(Ticket, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True)
    beginDate = models.DateTimeField()
    endDate = models.DateTimeField()
    state = models.CharField(max_length=15)