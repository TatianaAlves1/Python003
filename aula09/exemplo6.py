#Abertura de um arquivo chamado dados2.txt
#ler o nome de 10 pessoas e gravar no arquivo
try:
    txt = open("aula09/dados2.txt","w+")
    for i in range(1,11):
        nome = input("Informe o nome da pessoa:")
        txt.write(f"{i} - Nome:{nome}\n")
except:
    print("Não foi possível encontrar o arquivo!")
else:
    txt.seek(0)
    print(txt.read())
    txt.close()

