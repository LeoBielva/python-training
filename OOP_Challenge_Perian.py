#For this challenge, create a bank account class that has two attributes:
#owner
#balance
#and two methods:

#deposit
#withdraw
#As an added requirement, withdrawals may not exceed the available balance.

# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
    owner = 'Jose'
    balance = 666
    new_balance = 0

    def __str__(self):
        return "The account owner is{} \nYour balance is {}".format(Account.owner, Account.balance)

    def deposit(self, deposit):
        Account.new_balance = deposit + Account.balance
        print("Deposit successful! \nYour new balance is {}".format(Account.new_balance))

    def withdraw(self, withdraw):
        Account.new_balance = withdraw - Account.balance
        if withdraw <= Account.balance:
            print("Please take your {} bucks \nNew balance is {}".format(withdraw, Account.new_balance))
            return withdraw - Account.balance
        else:
            return "Insufficient founds"




my_account = Account()
print(my_account)
print('\n'*2)
my_account.deposit(1000)
my_account.withdraw(10000)



