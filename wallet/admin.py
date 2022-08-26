from django.contrib import admin
from .models import Account, Customer,Transaction,Thirdparty,Notification,Reward,Loan,Reciept, Wallet,Card
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","age","email","nationality","occupation","profile_picture","gender","phonenumber")
    search_fields=("first_name","last_name","age","email","nationality","occupation","profile_picture","gender","phonenumber")
admin.site.register(Customer,CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
        list_display=("currency","customer","balance","pin","amount")
        search_fields=("currency","customer","balance","pin","amount")
admin.site.register(Wallet,WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
     list_display=("account_type","account_number","balance","description")
     search_fields=("account_type","account_number","balance","description")
admin.site.register(Account,AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
      list_display=("date_time","source","value","amount","status")
      search_fields=("date_time","source","value","amount","status")
admin.site.register(Transaction,TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
      list_display=("card_name","card_number","expiry_date","issuer","account","date_issued")
      search_fields=("card_name","card_number","expiry_date","issuer","account","date_issued")
admin.site.register(Card,CardAdmin)

class ThirdpartyAdmin(admin.ModelAdmin):
      list_display=("thirdparty_name","transaction_cost","currency","account")
      search_fields=("thirdparty_name","transaction_cost","currency","account")
admin.site.register(Thirdparty,ThirdpartyAdmin)

class NotificationAdmin(admin.ModelAdmin):
      list_display=("message","title")
      search_fields=("message","title")
admin.site.register(Notification,NotificationAdmin)

class RecieptAdmin(admin.ModelAdmin):
      list_display=("amount","dateTime","transaction","reciept_type")
      search_fields=("amount","dateTime","transaction","reciept_type")
admin.site.register(Reciept,RecieptAdmin)

class LoanAdmin(admin.ModelAdmin):
      list_display=("loan_term","amount","payment_due","purpose","interest_rate")
      search_fields=("loan_term","amount","payment_due","purpose","interest_rate")
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
      list_display=("advertisement","points","customer_id","name","tickets")
      search_fields=("advertisement","points","customer_id","name","tickets")
admin.site.register(Reward,RewardAdmin)




















    


















