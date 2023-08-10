#ler a idade de um funcionário e tratar possíveis números negativos ou valores acima de 130


idade = int(input("Informe sua idade:"))
if idade<0 or idade>=130:
    raise Exception("Valor informado está incorreto")