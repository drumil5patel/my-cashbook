from CashBook1.models import *
from django import forms


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["account_name", "cur"]


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ["data_date", "narration", "cd", "amount", "account_id"]
