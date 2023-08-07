#criar uma lista de notas
notas = [6.25,2,10,9,8.8]
#valor máximo de uma nota da lista
print("Maior valor:",max(notas))
#Valor mínimo de uma nota da lista
print("Menor valor:",min(notas))
#Quantidade de itens na lista de notas
print("Quantidade de notas:",len(notas))
#Soma total das notas da lista
print("Soma das notas:",sum(notas))
#Mostrar média das notas da lista
print(f"Média aritmética:{sum(notas)/len(notas):.2f}")
#Operador in
print(11 in notas)
#loop for com listas
print(notas)
for i in notas:
    print(i,end=" ")
#leia 5 notas utilizando lista e estrutura de repetição
print("\n")
notas2 = []
for i in range(5):
    num = float(input("Informe a nota:"))
    notas2.append(num)

print("Todas as notas informadas:",notas2)
print("A quantidade de notas:",notas2)
print("A soma das notas é:",sum(notas2))

#leia uma quantidade de notas determinada pelo usuário e faça a soma dos valores digitados
qtd = int(input("Informe a quantidaded de notas:"))
cont = 1
notas3 = []
#adicionar somente notas de zero até dez
while cont<=qtd:
    num = float(input("Informe a nota:"))
    if num>=0 and num<=10:
        notas3.append(num)
    else:
       continue
    cont +=1
print("Total é:",sum(notas3))

