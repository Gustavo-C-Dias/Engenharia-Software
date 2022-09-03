import sqlite3
import matplotlib.pyplot as plt

def banco_dado (imc, peso, altura):
    conexao = sqlite3.connect('user.bd')
    cursor = conexao.cursor()

    def inserir_valor (imc, peso, altura, id_usuario):
        cursor.execute("""
        Insert into valores (imc, peso, altura, id_usuario) values (?,?,?,?)
        """, (imc, peso, altura, id_usuario))
        conexao.commit()
    
    def inserir_pessoas(login, senha):
        cursor.execute("""
        Insert into usuario(cpf, senha) values (?,?)
        """, (login, senha))
        conexao.commit()
    
    def consulta_usuario (login, senha):
        cursor.execute("""
        Select id from usuario where cpf = ? and senha = ?
        """, (login, senha))
        id_usuario = cursor.fetchall()
        id_usuario = id_usuario[0]

        id_usuario = int(','.join(map(str, id_usuario)))
        return id_usuario
    
    def gerar_grafico (id_usuario):
        cursor.execute ("""
        Select imc from valores where id_usuario = ?
        """, (id_usuario,))
        historico_imc = cursor.fetchall()

        cursor.execute ("""
        Select peso from valores where id_usuario = ?
        """, (id_usuario,))
        historico_peso = cursor.fetchall()

        print(historico_imc)
        print(historico_peso)
        plt.plot(historico_imc, historico_peso)
        plt.show()

        conexao.close()

    cadastro = int(input("Já possui cadastro ? \n  1 - Sim \n  2 - Não \n"))

    if (cadastro == 1):
        login = input("Informe seu CPF :")
        senha = input("Informe sua senha : ")

        id_usuario = consulta_usuario(login,senha)
        inserir_valor(imc, peso, altura, id_usuario)

    else :
        print("Podemos realizar um cadastro agora mesmo, para isso preciso de alguns dados")
        login = input("Informe seu CPF :")
        senha = input ("Digite a senha para acesso :")

        inserir_pessoas(login, senha)
        id_usuario = consulta_usuario(login,senha)
        inserir_valor(imc, peso, altura, id_usuario)

    gerar_grafico(id_usuario)

def classificacao (valor):
    print("\n---------------------- \n")
    print(f"Seu IMC é {valor:.2f}")

    if valor < 18.5 :
        print("Classificação : Abaixo do peso")
    elif valor >= 18.5 and valor < 25:
        print("Classificação: Peso ideal")
    elif valor >= 25 and valor < 30:
        print("Classificação: Sobrepeso")
    elif valor >= 30 and valor < 35:
        print("Classificação: Obesidade Grau I")
    elif valor >= 35 and valor < 40:
        print("Classificação: Obesidade Grau II")
    else :
        print("Classificação : Obesidade Grau III")

    print("\n---------------------- \n")
    
altura = float(input("Informe sua altura: "))
peso = float(input("Informe seu peso: "))

imc = peso / altura**2
classificacao(imc)

fluxo = int(input("Deseja armazenar esse valor ? \n  1 - Sim \n  2 - Não \n"))
if (fluxo == 1):
    banco_dado(imc, peso, altura)
else :
    print("Obrigado!")