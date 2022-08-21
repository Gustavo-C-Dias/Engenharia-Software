valor = int(input("Informe o valor a ser multiplicado: "))
resultado = 0

def multiplicacao (valor, multiplicacao):
    resultado = valor*multiplicacao
    print(f"{valor} x {multiplicacao} = {resultado}")

for i in range (1,11):
    multiplicacao(valor,i)