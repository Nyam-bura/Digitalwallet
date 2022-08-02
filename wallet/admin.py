from django.contrib import admin
from .models import Account, Customer,Currency, Transaction,Thirdparty,Notification,Rewards,Loan,Reciept, Wallet,Card
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","age","email","nationality","occupation","profile_picture","gender","phonenumber")
    search_fields=("first_name","last_name","age","email","nationality","occupation","profile_picture","gender","phonenumber")
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Currency)
# admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Thirdparty)
admin.site.register(Notification)
admin.site.register(Rewards)
admin.site.register(Loan)
admin.site.register(Reciept)
admin.site.register(Wallet)
admin.site.register(Card)











