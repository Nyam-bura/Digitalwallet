
from django.shortcuts import render
from rest_framework import viewsets
from wallet.models import Account, Card, Customer, Loan, Notification, Reciept, Transaction, Wallet
from .serializers import AccountSerializer, CardSerializer, CustomerSerializer, LoanSerializer, NotificationSerializer, RecieptSerializer, TransactionSerializer, WalletSerializer

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class RecieptViewSet(viewsets.ModelViewSet):
    queryset = Reciept.objects.all()
    serializer_class = RecieptSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
