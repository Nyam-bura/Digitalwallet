from errno import EALREADY
import re
from django.shortcuts import render
from wallet.models import Customer
from .models import Account, Card, Customer, Loan, Notification, Reciept, Reward, Thirdparty, Transaction, Wallet
from .forms import AccountRegistrationForm, CardRegistrationForm, CustomerRegistrationForm, LoanRegistrationFOrm, NotificationRegistrationForm, RecieptRegistrationForm, RewardRegistrationForm, ThirdPartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm
# Create your views here.

def register_customer(request):
    if request.method == "POST":
            form = CustomerRegistrationForm(request.POST)
            if form.is_valid():
                form.save
            else:
                form = CustomerRegistrationForm()
            return render(request,"wallet/register_customer.html",{"form":form})

def list_customer(request):
    customer= Customer.objects.all()
    return render(request,"customers_list.html",{"customers":customer})





def register_wallet(request):
    if request.method == "POST":
        form = WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save
        else:
            form = WalletRegistrationForm()
            return render(request,"wallet/register_wallet.html",{"form":form})

def list_wallet(request):
    wallets = Wallet.objects.all()
    return render(request,"wallets_list.html",{"wallet":wallets})

def register_account(request):
    if request.method == "POST":
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save
        else:
            form = AccountRegistrationForm()
            return render(request,"wallet/register_wallet.html",{"form":form})

def list_account(request):
    accounts = Account.objects.all()
    return render(request,"accounts_list.html",{"accounts":accounts})

def register_transaction(request):
    if request.method =="POST":
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save
        else:
            form = TransactionRegistrationForm()
            return render(request,"wallet/transaction.html/",{"form":form})

def list_transactions(request):
    transactions = Transaction.objects.all()
    return render(request,"transactions_list.html",{"transactions":transactions})



def register_card(request):
    if request.method =="POST":
        form = CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save
        else:
            form = CardRegistrationForm()
            return render(request,"wallet/card.html/",{"form":form})

def list_cards(request):
    cards = Card.objects.all()
    return render(request,"cards_list.html",{"cards":cards})


def register_thirdparty(request):
    if request.method =="POST":
        form = ThirdPartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save
        else:
            form = ThirdPartyRegistrationForm()
            return render(request,"wallet/thirdparty.html",{"form":form})

def list_parties(request):
    parties = Thirdparty.objects.all()
    return render(request,"parties_list.html",{"parties":parties})

    
def register_notification(request):
    if request.method =="POST":
        form = NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save
        else:
            form = NotificationRegistrationForm()
            return render(request,"wallet/notification.html/",{"form":form})

def list_notificatios(request):
    notifications = Notification.objects.all()
    return render(request,"notifications_list.html",{"notifications":notifications})

def register_reciept(request):
    if request.method =="POST":
        form = RecieptRegistrationForm(request.POST)
        if form.is_valid():
            form.save
        else:
            form = RecieptRegistrationForm()
            return render(request,"wallet/reciept.html/",{"form":form})

def list_reciepts(request):
    reciepts = Reciept.objects.all()
    return render(request,"reciepts_list.html",{"reciepts":reciepts})


    
def register_loan(request):
    if request.method =="POST":
        form  = LoanRegistrationFOrm(request.POST)
        if form.is_valid():
            form.save
        else:
            form = LoanRegistrationFOrm()
            return render(request,"wallet/loan.html/",{"form":form})

def list_loans(request):
    loans = Loan.objects.all()
    return render(request,"loans_list.html",{"loans":loans})


            

def register_reward(request):
    if request.method == "POST":
        form = RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save
        else:
            form = RewardRegistrationForm()
            return render(request,"wallet/reward.html/",{"form":form})

def list_rewards(request):
    rewards = Reward.objects.all()
    return render(request,"rewards_list.html",{"rewards":rewards})



