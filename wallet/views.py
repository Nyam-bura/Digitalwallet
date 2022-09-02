from django.shortcuts import render
from .forms import AccountRegistrationForm, CardRegistrationForm, CustomerRegistrationForm, LoanRegistrationFOrm, NotificationRegistrationForm, RecieptRegistrationForm, RewardRegistrationForm, ThirdPartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm
# Create your views here.

def register_customer(request):
    form = CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form":form})


def register_wallet(request):
    form = WalletRegistrationForm()
    return render(request,"wallet.html/",{"form":form})

def register_account(request):
    form = AccountRegistrationForm()
    return render(request,"account.html/",{"form":form})

def register_transaction(request):
    form = TransactionRegistrationForm()
    return render(request,"transaction.html/",{"form":form})

def register_card(request):
    form = CardRegistrationForm()
    return render(request,"transaction.html/",{"form":form})

def register_thirdparty(request):
    form = ThirdPartyRegistrationForm()
    return render(request,"thirdparty.html/",{"form":form})

def register_notification(request):
    form = NotificationRegistrationForm()
    return render(request,"notification.html/",{"form":form})

def register_reciept(request):
    form = RecieptRegistrationForm()
    return render(request,"reciept.html/",{"form":form})
    
def register_loan(request):
    form = LoanRegistrationFOrm()
    return render(request,"loan.html/",{"form":form})

def register_reward(request):
    form = RewardRegistrationForm()
    return render(request,"reward.html/",{"form":form})
