#Exemplo da função range()
print(list(range(2,20)))
print(list(range(10)))
print(list(range(10,100,5)))
print("-"*50)
#Loop for
for i in range(10):
    print(i, end=" ")
print("\nValor final do contador:",i)
print("-"*50)
#contagem de 20 até 30 usando laço for
for x in range(20,31):
    print(x,end=" ")
#contagem 10 até zero usando o laço for
for i in range(10,-1,-1):
    print(i,end=" ")
#Leia 5 números inteiros e mostre uma mensagem quando o número for par
# for i in range(5):
#     num = int(input("Informe o valor:"))
#     if num%2==0:
#         print("O valor informado é par")
#Leia 5 números inteiros e some somente os valores ímpares e mostre a quantidade de ímpares
# soma = 0
# for i in range(5):
#     num = int(input("Informe um valor:"))
#     if num%2!=0:
#         soma +=num    
# print("A soma dos ímpares é:",soma)

soma = 0
cont = 0
for i in range(5):
    num = int(input("Informe um valor:"))
    if num%2!=0:
        soma +=num
        cont +=1         
print("A soma dos ímpares é:",soma)
print("A quantidade de ímpares é:",cont)
#Mostre a média aritmética dos ímpares
print(f"A média de ímpares é {soma/cont:.2f}")