from asyncore import read
from django.db import models
from django.utils import timezone
from datetime import datetime
from random import choices
from unicodedata import name

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=10)
    address = models.TextField()
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    age = models.PositiveSmallIntegerField()
    nationality =models.CharField(max_length=30)
    occupation=models.CharField(max_length=30)
    profile_picture=models.ImageField(upload_to='profile_pictures/',null=True)
    date_created = models.DateTimeField(default=timezone.now)
    dob =models.DateField()
    GENDER_CHOICES =(
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True)

class Wallet(models.Model):
    currency=models.CharField(max_length=50)
    customer = models.ForeignKey(default=1,on_delete=models.CASCADE,to=Customer)
    balance = models.BigIntegerField()
    pin = models.PositiveSmallIntegerField(null=True)
    amount =models.IntegerField()

class Account(models.Model):
    account_type= models.CharField(max_length=20, null=True)
    account_number = models.IntegerField()
    balance = models.IntegerField()
    description = models.TextField()
    # wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE)c

class Transaction(models.Model):
    description = models.TextField(null=True)
    date_time = models.DateTimeField(null=True)
    source = models.URLField()
    value = models.IntegerField()
    amount = models.IntegerField()
    status = models.CharField(max_length=20)
    transaction_ref = models.CharField(max_length=10)
    origin = models.ForeignKey(default=1,on_delete=models.CASCADE,to=Account,related_name='Transactions_account')
    bonus_credit = models.BooleanField(null=True)
    destination = models.URLField(null=True)


class Card(models.Model):
    card_name= models.CharField(max_length=100,null=True)
    card_number = models.CharField(max_length=100)
    expiry_date = models.DateTimeField(default=datetime.now)
    issuer = models.CharField(max_length=100)
    account = models.ForeignKey(default=1,on_delete=models.CASCADE,to=Account,related_name='Card_account')
    date_issued = models.DateTimeField(default=datetime.now)

class Thirdparty(models.Model):
    thirdparty_name = models.CharField(max_length=100)
    transaction_cost = models.IntegerField()
    currency = models.CharField(max_length=100)
    account = models.ForeignKey(default=1,on_delete=models.CASCADE,to=Account,related_name='Thirdparty_account')
    location = models.CharField(max_length=100, null=True)

class Notification(models.Model):
    message = models.TextField()
    title = models.CharField(max_length=10)
    name = models.CharField(max_length=10,null=True)
    status = models.BooleanField(null=True)
    date_time = models.DateTimeField(null=True)

class Reciept(models.Model):
    amount = models.IntegerField()
    dateTime = models.DateTimeField(default=datetime.now)
    transaction = models.PositiveIntegerField()
    reciept_type = models.CharField(max_length=100)
    file = models.FileField(null=True)
    # description = models.BigIntegerField()

class Loan(models.Model):
    # wallet = models.ForeignKey(default=1,on_delete=models.CASCADE,to=Wallet)
    loan_term = models.IntegerField()
    amount = models.IntegerField()
    payment_due = models.DateTimeField(default=datetime.now)
    loan_balance = models.IntegerField()
    purpose = models.CharField(max_length=100)
    interest_rate = models.IntegerField()

class Reward(models.Model):
    points = models.IntegerField()
    customer_id = models.IntegerField()
    name = models.CharField(max_length=30)
    advertisement = models.CharField(max_length=100)
    tickets = models.CharField(max_length=100)



