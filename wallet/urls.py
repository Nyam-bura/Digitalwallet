# from ast import pattern
from django.urls import path
from .views import register_account, register_card, register_customer, register_loan, register_notification, register_reciept, register_reward, register_thirdparty, register_transaction, register_wallet

urlpatterns= [
    path("register/",register_customer,name="registration"),
    path("wallet/",register_wallet,name="wallet"),
    path("account/",register_account,name="account"),
    path("transaction/",register_transaction,name="transaction"),
    path("card/",register_card,name="card"),
    path("thirdparty/",register_thirdparty,name="thirdparty"),
    path("notification/",register_notification,name="notification"),
    path("reciept/",register_reciept,name="reciept"),
    path("loan/",register_loan,name="loan"),
    path("reward/",register_reward,name="reward"),








]