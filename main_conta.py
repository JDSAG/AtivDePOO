from ContaBanco import * 
#=======  Conta bancaria  =======#
conta = ContaBancaria('12345-6','Maria',1250)

print (f"Numero da conta: {conta.number}")
print (f"Nome do Titular: {conta.nome}")
print (f"Saldo da conta: {conta.saldo}")

conta.depositar(500)   #Deposito Valido
conta.sacar(200)       #Saque Valido tbm 
conta.sacar(2000)      #Saque Invalido (Por ser insuficiente)
conta.depositar(-100)  #Deposito invalido (Por ser negativo) 

print (f"Numero da conta: {conta.number}")
print (f"Nome do Titular: {conta.nome}") 
print (f"Saldo da conta: {conta.saldo}") #Pós mudanças 




