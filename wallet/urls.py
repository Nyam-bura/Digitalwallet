# from ast import pattern
from django.urls import path
from .views import list_account, list_cards, list_customer, list_loans, list_notificatios, list_parties, list_reciepts, list_rewards, list_transactions, list_wallet, register_account, register_card, register_customer, register_loan, register_notification, register_reciept, register_reward, register_thirdparty, register_transaction, register_wallet

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
    path("customers/",list_customer,name="customer_list"),
    path("wallets/",list_wallet,name="wallets_list"),
    path("accounts/",list_account,name="accounts_list"),
    path("transactions/",list_transactions,name="transactions_list"),
    path("cards/",list_cards,name="cards_list"),
    path("parties/",list_parties,name="parties_list"),
    path("notifications/",list_notificatios,name="notifications_list"),
    path("reciepts/",list_reciepts,name="reciepts_list"),
    path("loans/",list_loans,name="loans_list"),
        path("rewards/",list_rewards,name="rewards_list"),
















]