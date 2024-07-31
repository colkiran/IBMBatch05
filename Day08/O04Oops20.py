
from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self):
        print("Accont Ctor.....")
    @abstractmethod
    def get_balance(self):
        pass


class Savings(Account):

    def deposit(self):
        print('Amount credited into the account successfully....')

    def get_balance(self):
        print("The balance in the account ending #### is ########")

sav1 = Savings()
sav1.deposit()
sav1.get_balance()