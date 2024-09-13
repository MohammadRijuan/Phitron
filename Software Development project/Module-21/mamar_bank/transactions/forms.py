from django import forms
from . models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount','transaction_type']


    def __init__(self,*args,**kwargs):
        self.account = kwargs.pop('account')  #account take ber kore niye asbo..mane capture korrlam
        super().__init__(*args,**kwargs)

        self.fields['transaction_type'].disabled = True # ei field disable thakbe r user teke hide kora thakbe
        self.fields['transaction_type'].widget = forms.HiddenInput()

        def save(self,commit=True):
            self.instance.account = self.account
            self.instance.balance_after_transaction = self.account.balance 

            return super().save()
        

class DepositForm(TransactionForm):
    def clean_amount(self): #amount field ke filter korbo...r j field ke use kora lagbe sey field ke clean add kore cll korbo..jmn clean_balance
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount') # user er fillup kora form teke amra amount  field er value ke niye aslam 

        if amount < min_deposit_amount :
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount}$'
            )
        

class WithdrawForm(TransactionForm):

    def clean_amount(self):
        account = self.account
        min_withdraw_amount = 500
        max_withdraw_amount = 20000
        balance = account.balance
        amount = self.cleaned_data.get('amount')

        if amount < min_withdraw_amount :
            raise forms.ValidationError(
                f'You Can withdraw at least {min_withdraw_amount}$'
            )
        
        if amount < max_withdraw_amount :
            raise forms.ValidationError(
                f'You Can withdraw at most {min_withdraw_amount}$'
            )
        
        return amount
    
class LoanRequestForm(TransactionForm):
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')

        return amount