import abc
from dataclasses import dataclass


@dataclass
class Account(abc.ABC):
    agency : int
    account : int
    balance : float = 0

    @abc.abstractmethod
    def withdraw(self, value: float) -> float: ...

    def deposit(self, value: float) -> float:
        self.balance += value
        self.details(f'(DEPOSIT {value})')
        return self.balance

    def details(self, msg: str = '') -> None:
        print(f'account : {self.account} has a balance of {self.balance:.2f} {msg}')
        print('--')

@dataclass
class SavingsAcount(Account):
    def withdraw(self, value):
        value_after_withdraw = self.balance - value

        if value_after_withdraw >= 0:
            self.balance -= value
            self.details(f'(WITHDRAW {value})')
            return self.balance

        print('Impossible to do this operation')
        self.details(f'(WITHDRAW RECUSED {value})')
        return self.balance

@dataclass
class CheckingAccount(Account):
    limit : float = 0

    def withdraw(self, value: float) -> float:
        value_after_withdraw = self.balance - value
        max_limit = -self.limit

        if value_after_withdraw >= max_limit:
            self.balance -= value
            self.details(f'(WITHDRAW {value})')
            return self.balance

        print('Impossible to withdraw this value')
        print(f'Your limit is {-self.limit:.2f}')
        self.details(f'(Withdraw recused {value})')
        return self.balance
    