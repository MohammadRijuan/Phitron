from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView,ListView
from .models import Transaction,Transfer
from django.contrib.auth.mixins import LoginRequiredMixin

# LoginRequiredMixin ata amdr logged in user ke safe rakhe...

from .forms import DepositForm,WithdrawForm,LoanRequestForm
from . constants import DEPOSIT,WITHDRAWAL,LOAN,LOAN_PAID,TRANSFER
from django.contrib import messages
from datetime import datetime
from django.db.models import Sum
from django.shortcuts import redirect,render,get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import FormView
from . forms import TransferForm,DepositForm,WithdrawForm
from bankrupt_app.models import IsBankrupt
from accounts.models import UserBankAccount
from django.contrib.auth.decorators import login_required


# Create your views here.

# ei view ke inherit kore deposit,withdraw,loan request korbo
class TransactionCreateMixin(LoginRequiredMixin,CreateView):
    template_name = 'transactions/transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('transaction_report')
    
    def get_form_kwargs(self): #ata amdr data pass korbe amdr form ke
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account' : self.request.user.account,
        })
        return kwargs
    
    def get_context_data(self, **kwargs):  # amdr front end ke show korbe
        context = super().get_context_data(**kwargs)
        context.update({
            'title' : self.title
        })
        return context
        

class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Deposit'

    def get_initial(self):
        initial = {'transaction_type': DEPOSIT}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        # if not account.initial_deposit_date:
        #     now = timezone.now()
        #     account.initial_deposit_date = now
        account.balance += amount # amount = 200, tar ager balance = 0 taka new balance = 0+200 = 200
        account.save(
            update_fields=[
                'balance'
            ]
        )

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )
        # send_transaction_email(self.request.user, amount, "Deposite Message", "transactions/deposite_email.html")
        return super().form_valid(form)


class WithdrawMoneyView(TransactionCreateMixin):
    form_class = WithdrawForm
    title = 'Withdraw Money'

    def get_initial(self):
        initial = {'transaction_type': WITHDRAWAL}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        
        bankrupt_status = IsBankrupt.objects.first()
        if bankrupt_status and bankrupt_status.is_bankrupt:
            messages.error(self.request,'The bank is bankrupt.Withdrawal are disabled')
            return redirect('withdraw_money')
        

        if amount > self.request.user.account.balance:
            messages.error(self.request, 'Insufficient funds.')
            return redirect('withdraw_money')
        
        self.request.user.account.balance -= form.cleaned_data.get('amount')
        self.request.user.account.save(update_fields=['balance'])

        messages.success(
            self.request,
            f'Successfully withdrawn {"{:,.2f}".format(float(amount))}$ from your account'
        )

        return super().form_valid(form)
    

class LoanRequestView(TransactionCreateMixin):
    form_class = LoanRequestForm
    title = 'Request for loan'

    def get_initial(self):
        initial = {'transaction_type' : LOAN} #contants.py er Withdrawal er maddhome select kora
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        current_loan_count = Transaction.objects.filter(account = self.request.user.account, transaction_type = LOAN ,loan_approve = True).count()

        if current_loan_count >=3:
            return HttpResponse("You have crossed Your limits")

        messages.success(self.request,f'loan request for amount{amount}$')
        return super().form_valid(form)
    


class TransactionReportView(LoginRequiredMixin,ListView):
    template_name= 'transactions/transaction_report.html'
    model = Transaction
    balance = 0

    def get_queryset(self):
        #jodi user kono type filter na kore taile tar total transaction report dekabo
        queryset = super().get_queryset().filter(
            account = self.request.user.account
        )
        # start date r end date ta ber kore anlam
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')
        
        # amra jehetu GET kore date gulo string format e paisi tai segulo ke (strpttme) diye date object e convert korci

        if start_date_str and end_date_str:
            start_date  = datetime.strptime(start_date_str,"%Y-%M-%d").date()
            end_date  = datetime.strptime(start_date_str,"%Y-%M-%d").date()
            
            queryset = queryset.filter(timestamp__date__gte = start_date, timestamp__date__lte =end_date)
            
            
            self.balance = Transaction.objects.filter(timestamp__date__gte = start_date , timestamp__date__lte = end_date).aggregate(Sum('amount'))
            ['amount_sum']

        else:
            self.balance = self.request.user.account.balance

        return queryset.distinct() #unique queryset hote hobe
    
    def get_context_data(self, **kwargs):  # amdr front end ke show korbe
        context = super().get_context_data(**kwargs)
        context.update({
            'account' : self.request.user.account
        })
        return context


class PayLoanView(LoginRequiredMixin,View):

    def get(self,request, loan_id):
        loan = get_object_or_404(Transaction, id = loan_id)

        if loan.loan_approve:  #ekjon user loan pay korte parbe tokon e jokon tar loan approve hobe
            user_account = loan.account #loan account e user account reke dilam

            if loan.amount < user_account.balance:
                user_account.balance -= loan.amount
                loan.balance_after_transaction = user_account.balance

                user_account.save()
                loan.transaction_type = LOAN_PAID
                loan.save()

                return redirect('loan_list')
            else:
                messages.success(self.request,f'loan amount is greater than available balance')
                return redirect('loan_list')
             
    

class LoanListView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/loan_request.html'
    context_object_name = 'loans' #ei name access korar jnno...kono kicu na dile Transaction or object  diye cl hoto

    def get_queryset(self):
        user_account = self.request.user.account
        queryset = Transaction.objects.filter(account= user_account, transaction_type = LOAN )
        return queryset
    

class TransferMoneyView(FormView):
    template_name= 'tansactions/transfer_form.html'
    form_class = TransferForm
    success_url = 'home'

    def form_valid(self,form):
        sender_account = self.request.user.account
        receiver_account = form.cleaned_data['receiver']
        amount = form.cleaned_data['amount']

        if sender_account.balance < amount :
            messages.success(self.request,'You dont have enough balance to transfer')

        else:
            sender_account.balance -= amount
            receiver_account.balance += amount
            sender_account.save()
            receiver_account.save()

            Transfer.objects.create(sender = sender_account, receiver = receiver_account,amount=amount)
            messages.success(self.request, f'Successfully Transferred {amount}$')

        return super().form_valid(form)
    

    def form_invalid(self,form):
        messages.success(self.request,'Trnasfer Failed ! Please Check your details')
        return super().form_invalid(form)

@login_required
def transfer_money(request):
    form = TransferForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            sender_account = request.user.account
            receiver_account_no = form.cleaned_data['receiver_account_no']
            receiver_account = UserBankAccount.objects.get(account_no=receiver_account_no)
            amount = form.cleaned_data['amount']

            if sender_account.balance < amount:
                messages.error(request, 'Insufficient balance. Transfer failed.')
            else:
                sender_account.balance -= amount
                receiver_account.balance += amount
                sender_account.save()
                receiver_account.save()

                Transfer.objects.create(sender=sender_account, receiver=receiver_account, amount=amount)
                
                
                # to show it to into my transaction report
                Transaction.objects.create(account=sender_account,transaction_type=TRANSFER, amount=-amount, balance_after_transaction=sender_account.balance)
                Transaction.objects.create(account=receiver_account,transaction_type=TRANSFER, amount=amount, balance_after_transaction=receiver_account.balance)
                messages.success(request, f'Successfully transferred ${amount} to Account No: {receiver_account_no}.')
                
                return redirect('home')
    return render(request, 'transactions/transfer_form.html', {'form': form})
        