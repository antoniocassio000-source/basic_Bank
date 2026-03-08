from accounts import *
from bank import *
from people import *
'''
Basicamente vc pode criar um cliente e uma conta
'''
conta1 = CheckingAccount(2,123,0,123)
cliente1 = Client(18, "luiz", conta1)

pessoa2 = People(12,"cassio")
conta2 = SavingsAcount(1,2)
cliente2 = Client(12, "cassio", conta2)
'''
Na estrutura do banco vc pode adicionar agencias, clientes e contas
'''
banco_1 = Bank()
banco_1.agencies.extend([1,2])
banco_1.clients.extend([cliente1,cliente2])
banco_1.accounts.extend([conta1,conta2])
'''
Aqui vc introduz um cliente e uma conta na funcao authenticate, podendo fazer açoes de saque e
deposito se estiver logado no banco
'''
if banco_1.authenticate(cliente1,conta1):
        conta1.deposit(123)
        conta1.withdraw(123)

if banco_1.authenticate(cliente2, conta2):
        conta2.deposit(12635)
        conta2.withdraw(1231)

