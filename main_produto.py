from Produto import * 

produto = Produto('Banana',1.99,30) 

print (f'Nome do Produto: {produto.nome}')
print (f'Preço do Produto: {produto.preco}')
print (f'Estoque do Produto: {produto.estoque}') 

produto.adicionar(20) #Adicionar
print (f'Estoque do Produto: {produto.estoque}') 

produto.adicionar(-20) #Invalidar a adição (Valor Negativo)
print (f'Estoque do Produto: {produto.estoque}') 

produto.remover(10) #Remover 
print (f'Estoque do Produto: {produto.estoque}') 

produto.remover(100) #Invalidar a remoção (Estoque Insuficiente)
print (f'Estoque do Produto: {produto.estoque}') 


