
try:
    print(x)
except Exception as e:
    print("Falha ao acessar a variável")
    print(e)
else:
    print("Parabéns!!! Seu script funcionou perfeitamente.")
finally:
    print("Fim do tratamento de exceções")

