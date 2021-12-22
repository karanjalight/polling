from django.contrib import admin
from . models import Question, Choice #, Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# class AccountInLine(admin.StackedInline):
#   model = Account
#   can_delete = False
#   verbose_name_plural = "Accounts"

# class CustomizedUserAdmin (UserAdmin):
#   inlines = (AccountInLine, )

#admin.site.register(Account)
#admin.site.unregister(User)
#admin.site.register(User, CustomizedUserAdmin)
#admin.site.register(Account)
admin.site.register(Question)
admin.site.register(Choice)

 