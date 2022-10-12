# from ast import pattern
from django.urls import path
from .views import customer_profile, account_profile, rewards_profile, loan_profile, reciepts_profile,notification_profile, parties_profile, cards_profile, transactions_profile,  edit_profile, list_account, list_cards, list_customer, list_loans,wallet_profile, list_notifications, list_parties, list_reciepts, list_rewards, list_transactions, list_wallet, register_account, register_card, register_customer, register_loan, register_notification, register_reciept, register_reward, register_thirdparty, register_transaction, register_wallet

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
    path("walletss/",list_wallet,name="wallets_list"),
    path("accounts/",list_account,name="accounts_list"),
    path("transactions/",list_transactions,name="transactions_list"),
    path("cards/",list_cards,name="cards_list"),
    path("parties/",list_parties,name="parties_list"),
    path("notifications/",list_notifications,name="notifications_list"),
    path("reciepts/",list_reciepts,name="reciepts_list"),
    path("loans/",list_loans,name="loans_list"),
    path("rewards/",list_rewards,name="rewards_list"),

    path("customers/<int:id>/",customer_profile,name="customer_profile"),
    # path("wallets/<int:id>/",wallet_profile,name="wallet_profile"),
    # path("accounts/<int:id>/",account_profile,name="account_profile"),
    # path("transactions/<int:id>/",transactions_profile,name="transactions_profile"),
    # path("cards/<int:id>/",cards_profile,name="cards_profile"),
    # path("parties/<int:id>/",parties_profile,name="parties_profile"),
    # path("parties/<int:id>/",notification_profile,name="parties_profile"),
    # path("cards/<int:id>/",cards_profile,name="cards_profile"),
    # path("reciepts/<int:id>/",reciepts_profile,name="reciepts_profile"),
    # path("loan/<int:id>/",loan_profile,name="loan_profile"),
    # path("rewards/<int:id>/",rewards_profile,name="rewards_profile"),






    path("customerss/edit/<int:id>/",edit_profile,name="edit_profile"),
    # path("wallets/edit/<int:id>/",edit_profile,name="edit_wallet"),
    # path("accounts/edit/<int:id>/",edit_account,name="edit_account"),
    # path("transactions/edit/<int:id>/",edit_transactions,name="edit_transactions"),
    # path("cards/edit/<int:id>/",edit_cards,name="edit_cards"),
    # path("parties/edit/<int:id>/",edit_parties,name="edit_parties"),
    # path("notifications/edit/<int:id>/",edit_notifications,name="edit_notifications"),
    # path("reciepts/edit/<int:id>/",edit_reciepts,name="edit_reciepts"),
    # path("loan/edit/<int:id>/",edit_loan,name="edit_loan"),
    # path("reward/edit/<int:id>/",edit_reward,name="edit_reward"),

























]