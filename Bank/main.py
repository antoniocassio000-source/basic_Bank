from accounts import *
from bank import *
from people import *

conta1 = CheckingAccount(2,123,0,123)
cliente1 = Client(18, "luiz", conta1)

pessoa2 = People(12,"cassio")
conta2 = SavingsAcount(1,2)
cliente2 = Client(12, "cassio", conta2)

banco_1 = Bank()
banco_1.agencies.extend([1,2])
banco_1.clients.extend([cliente1,cliente2])
banco_1.accounts.extend([conta1,conta2])

if banco_1.authenticate(cliente1,conta1):
        b.deposit(123)
        b.withdraw(123)

if banco_1.authenticate(cliente2, conta2):
        z.deposit(12635)
        z.withdraw(1231)