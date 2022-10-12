# from errno import EALREADY
# import re
from django.shortcuts import redirect, render
# from wallet.models import Customer
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
    customers= Customer.objects.all()
    return render(request,"customers_list.html",{"customers":customers})

def customer_profile(request, id):
    customer = Customer.objects.get(id=id)
    return render(request,"customer_profile.html",{"customer":customer})


def edit_profile(request,id):
    customer = Customer.objects.get(id=id)
    if request.method =="POST":
        form = CustomerRegistrationForm(request.POST, instance=customer)
        if form.is_valid():
            form.save
            return redirect("customer_profile", id=customer.id)
    else:
        form = CustomerRegistrationForm(instance=customer)
        return render(request,"edit_profile.html",{"form":form})




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

def wallet_profile(request, id):
    wallets = Wallet.objects.get(id=id)
    return render(request,"wallet_profile.html",{"wallets":wallets})

def edit_wallet(request,id):
    wallet = Wallet.objects.get(id=id)
    if request.method =="POST":
        form = WalletRegistrationForm(request.POST, instance=wallet)
        if form.is_valid():
            form.save
            return redirect("edit_wallet", id=wallet.id)
    else:
        form = WalletRegistrationForm(instance=wallet)
        return render(request,"edit_wallet.html",{"form":form})

    

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

def account_profile(request, id):
    accounts = Account.objects.get(id=id)
    return render(request,"account_profile.html",{"accounts":accounts})

def edit_account(request,id):
    account = Account.objects.get(id=id)
    if request.method =="POST":
        form = AccountRegistrationForm(request.POST, instance=account)
        if form.is_valid():
            form.save
            return redirect("edit_account", id=account.id)
    else:
        form = AccountRegistrationForm(instance=account)
        return render(request,"edit_account.html",{"form":form})

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

def transactions_profile(request, id):
    transactions = Transaction.objects.get(id=id)
    return render(request,"transactions_profile.html",{"transactions":transactions})

def edit_transactions(request,id):
    transacation = Transaction.objects.get(id=id)
    if request.method =="POST":
        form = TransactionRegistrationForm(request.POST, instance=transacation)
        if form.is_valid():
            form.save
            return redirect("edit_transactions", id=transacation.id)
    else:
        form = TransactionRegistrationForm(instance=transacation)
        return render(request,"edit_transactions.html",{"form":form})



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

def cards_profile(request, id):
    cards = Card.objects.get(id=id)
    return render(request,"cards_profile.html",{"cards":cards})

def edit_cards(request,id):
    cards = Card.objects.get(id=id)
    if request.method =="POST":
        form = CardRegistrationForm(request.POST, instance=cards)
        if form.is_valid():
            form.save
            return redirect("edit_cards", id=cards.id)
    else:
        form = CardRegistrationForm(instance=cards)
        return render(request,"edit_cards.html",{"form":form})


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

def parties_profile(request, id):
    parties = Thirdparty.objects.get(id=id)
    return render(request,"parties_profile.html",{"cards":parties})

def edit_parties(request,id):
    parties = Thirdparty.objects.get(id=id)
    if request.method =="POST":
        form = ThirdPartyRegistrationForm(request.POST, instance=parties)
        if form.is_valid():
            form.save
            return redirect("edit_parties", id=parties.id)
    else:
        form = ThirdPartyRegistrationForm(instance=parties)
        return render(request,"edit_parties.html",{"form":form})
    
def register_notification(request):
    if request.method =="POST":
        form = NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save
        else:
            form = NotificationRegistrationForm()
            return render(request,"wallet/notification.html/",{"form":form})

def list_notifications(request):
    notifications = Notification.objects.all()
    return render(request,"notifications_list.html",{"notifications":notifications})

def notification_profile(request, id):
    notifications = Notification.objects.get(id=id)
    return render(request,"notifications_profile.html",{"cards":notifications})

def edit_notifications(request,id):
    notifications = Notification.objects.get(id=id)
    if request.method =="POST":
        form = NotificationRegistrationForm(request.POST, instance=notifications)
        if form.is_valid():
            form.save
            return redirect("edit_notifications", id=notifications.id)
    else:
        form = NotificationRegistrationForm(instance=notifications)
        return render(request,"edit_notifications.html",{"form":form})

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

def reciepts_profile(request, id):
    reciepts = Reciept.objects.get(id=id)
    return render(request,"reciepts_profile.html",{"reciepts":reciepts})


def edit_reciepts(request,id):
    reciepts = Reciept.objects.get(id=id)
    if request.method =="POST":
        form = RecieptRegistrationForm(request.POST, instance=reciepts)
        if form.is_valid():
            form.save
            return redirect("edit_reciepts", id=reciepts.id)
    else:
        form = RecieptRegistrationForm(instance=reciepts)
        return render(request,"edit_reciepts.html",{"form":form})



    
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

def loan_profile(request, id):
    loans = Loan.objects.get(id=id)
    return render(request,"loan_profile.html",{"loans":loans})

def edit_loan(request,id):
    loans = Loan.objects.get(id=id)
    if request.method =="POST":
        form = LoanRegistrationFOrm(request.POST, instance=loans)
        if form.is_valid():
            form.save
            return redirect("edit_loan", id=loans.id)
    else:
        form = LoanRegistrationFOrm(instance=loans)
        return render(request,"edit_loan.html",{"form":form})


            

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

def rewards_profile(request, id):
    reward = Reward.objects.get(id=id)
    return render(request,"rewards_profile.html",{"reward":reward})

def edit_reward(request,id):
    reward = Reward.objects.get(id=id)
    if request.method =="POST":
        form = RewardRegistrationForm(request.POST, instance=reward)
        if form.is_valid():
            form.save
            return redirect("edit_rewards", id=reward.id)
    else:
        form = RewardRegistrationForm(instance=reward)
        return render(request,"edit_rewards.html",{"form":form})



