#ler nome e e-mail e armazenar no arquivos dados3.txt
try:
    txt = open("aula09/dados3.txt","a+",encoding='utf-8')
    nome  = input("Informe o nome:")
    email = input("Informe o e-mail:")
    txt.write(f"{nome:^15} - {email:^15}\n") 
except:
    print("Erro ao gravar os dados!!!")
