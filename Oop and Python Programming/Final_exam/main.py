from bank import *
from User import *
def main():

    Islami_Bank=Bank("Islami Bank Bangladesh Limited","Bahaddarhat",50000)

    admin=Admin('admin','abc@gmail.com','x',123)
    admin.bank=Islami_Bank
    Rijuan=Account_Holder('rijuan','rijuan@gmail.com','Bahaddarhat','savings')
    Rijuan.bank=Islami_Bank
    monju=Account_Holder('Monju','monju@gmail.com','chandgaon','savings')
    monju.bank=Islami_Bank

    print(Islami_Bank)

    currentuser=None

    while(True):
        if currentuser is None:
            print('please login or register(L/R):')
            opt=input("Are you admin  or user?: ")
            if opt=='user':
                option=input('login or register (L/R):')
                if option=='R':
                    name=input("Enter ur name: ")
                    email=input("Enter ur email: ")
                    address=input("Enter ur address: ")
                    account_type=input("Savings or current? (sav/cur): ")
                    
                    currentuser=Account_Holder(name,email,address,account_type)
                
                elif option=="L":
                    name=input('Enter ur name: ')
                    email=input('enter ur email: ')
                    match=False

                    for user in User.Accounts:
                       if isinstance(user, Account_Holder) and user.name == name and user.email == email:
                           currentuser = user
                           match = True
                           break
                    if not match:
                        print('\nYour information is incorrect!')

                else:
                    print("invalid option")
        
            elif opt =='admin':
                name=input('Enter ur name : ')
                password=int(input('Enter ur password : '))

                if name=="admin" and password==12345:
                    currentuser=admin
                else:
                    print('please check ur name and password again')
            else:
                print('invalid option')

        else:
            print('------Welcome back-----')
            if isinstance(currentuser,Account_Holder):
                print('------menu-----')
                print('1.Deposit')
                print('2.Withdraw')
                print('3.Transaction History')
                print('4.Check balance')
                print('5.get loan')
                print('6.Transfer balance')
                print('7.logout')

                option=int(input('Enter ur options: '))

                if option==1:
                    money=int(input('Enter ur deposit money : '))
                    currentuser.deposit(money)
                
                elif option == 2:
                    money=int(input("Enter ur withdrawal money : "))
                    currentuser.withdraw_money(money)

                elif option == 3:
                    currentuser.show_transaction_history()

                elif option == 4:
                    currentuser.view_balance()

                elif option ==5:
                    money=int(input('Enter loan amount : '))
                    currentuser.getting_loan(money)

                elif option ==6:
                    name=input('Enter the account name : ')
                    amount=int(input('Enter ur amount : '))
                    currentuser.transfer_balance(name,amount)

                elif option== 7:
                    currentuser=None
                else:
                    print('invalid option')

            else:
                print('-----Admin Panel------')
                print('1.Create an account ')
                print('2.Delete a user account ')
                print('3.See all user ')
                print('4.total balance ')
                print('5.total loan ')
                print('6.loan feature ')
                print('7.Bankrupt ')
                print('8.logout ')

                option=int(input('Enter ur options : '))

                if option==1:
                    name=input('Enter ur name: ')
                    email=input('Enter ur email: ')
                    address=input('Enter ur address: ')
                    account_type=input("What is ur account type will be? (sav or cur) : ")
                    currentuser.create_an_account(name,email,address,account_type)

                elif option==2:
                    delete=input('Enter the index number of the user')
                    currentuser.delete_a_user(delete)

                elif option==3:
                    currentuser.view_users()
                
                elif option==4:
                     currentuser.total_bank_balance()

                elif option==5:
                    currentuser.show_total_loan()

                elif option==6:
                    permission=input('Do u want to switch on or off (on/off) : ')
                    if permission == 'on':
                       currentuser.loan_feature(permission)
                
                elif option == 7:
                    xyz=input('is someone steal the whole money of bank? (yes/no)')
                    if xyz=='yes':
                        currentuser.bankruptt(True)

                elif option==8:
                    currentuser=None

                else:
                    print(' Invalid option ')
                


                


    

                






if __name__ =='__main__':
    main()