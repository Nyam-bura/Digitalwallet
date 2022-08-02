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



class Currency(models.Model):
    amount= models.IntegerField()
    country_of_origin = models.CharField(max_length=24,null=True)

class Wallet(models.Model):
    currency=models.ForeignKey(Currency, on_delete=models.CASCADE,related_name='Wallet_currency')
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='Wallet_customer')
    balance = models.IntegerField()
    pin = models.TextField(max_length=6,null=True)
    status =models.CharField(max_length=20,null=True)
    amount =models.IntegerField()
    date =models.DateTimeField(default=timezone.now)

class Account(models.Model):
    account_type= models.CharField(max_length=20, null=True)
    account_number = models.IntegerField()
    balance = models.IntegerField()
    description = models.TextField()
    # wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE)

class Transaction(models.Model):
    # destination = models.ForeignKey()
    date_time = models.DateTimeField()
    source = models.URLField()
    value = models.IntegerField()
    amount = models.IntegerField()
    status = models.CharField(max_length=20)
    transaction_ref = models.CharField(max_length=10)

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

class Notification(models.Model):
    message = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

class Reciept(models.Model):
    amount = models.IntegerField()
    dateTime = models.DateTimeField(default=datetime.now)
    transaction = models.PositiveIntegerField()
    reciept_type = models.IntegerField()

class Loan(models.Model):
    # wallet = models.ForeignKey(default=1,on_delete=models.CASCADE,to=Wallet)
    loan_term = models.IntegerField()
    amount = models.IntegerField()
    payment_due = models.DateTimeField(default=datetime.now)
    loan_balance = models.IntegerField()
    purpose = models.CharField(max_length=100)
    interest_rate = models.IntegerField()

class Rewards(models.Model):
    points = models.IntegerField()
    customer_id = models.IntegerField()
    name = models.CharField(max_length=30)


