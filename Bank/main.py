from accounts import *
from bank import *
from people import *

b = CheckingAccount(2,123,0,123)
c = Client(18, "luiz", b)

x = People(12,"cassio")
z = SavingsAcount(1,2)
y = Client(12, "cassio", z)
v = Bank()
v.agencies.extend([1,2])
v.clients.extend([y,c])
v.accounts.extend([z,b])

if v.authenticate(y, z):
        z.deposit(12635)
        z.withdraw(1231)

if v.authenticate(c,b):
        b.deposit(123)
        b.withdraw(123)
       