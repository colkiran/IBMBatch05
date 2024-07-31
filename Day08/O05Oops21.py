
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Manager's job")


class Developer(Employee):

    def doJob(self):
        print("Developer's job")


def BankFun(emp):
    print("Bankjob Started.....")
    emp.doJob()
    print("Bankjob Ended.......")
    print("-" * 60)

mike = Manager()
dave = Developer()

BankFun(mike)       # does managers job
BankFun(dave)