package com.mycompany.sistemabancario;

import java.util.Scanner;

public class Menu {
    
   public static void menuInicial() {
        int opcao;
        String nome, sobrenome, cpf;

        Scanner teclado = new Scanner(System.in);

        System.out.println("----- Criação de conta -----");
        System.out.print("Nome: ");
        nome = teclado.nextLine();
        System.out.print("Sobrenome: ");
        sobrenome = teclado.nextLine();
        System.out.print("CPF: ");
        cpf = teclado.nextLine();

        Clientes cliente = new Clientes(nome, sobrenome, cpf);
        Contas conta = new Contas(12345, cliente);

        do {
            menuConta();
            opcao = teclado.nextInt();

            switch (opcao) {
                case 1:
                    System.out.print("\nSaldo: " + conta.getSaldo());
                    break;

                case 2:
                    double valorDeposito;
                    System.out.print("\nValor do deposito: R$ ");
                    valorDeposito = teclado.nextDouble();
                    conta.depositar(valorDeposito);
                    break;

                case 3:
                    double valorSaque;
                    System.out.print("\nValor do saque: R$ ");
                    valorSaque = teclado.nextDouble();
                    conta.sacar(valorSaque);
                    break;
                    
                case 4:
                    System.out.println("\n" + conta.getCliente());
                    break;
                    
                case 0:
                    System.out.println("\nObrigado por utilizar o sistema!");
                    break;
                    
                default:
                    System.out.println("Digite uma opção válida");
            }
        } while (opcao != 0);
    }

    public static void menuConta() {
        System.out.println("\n---------------------------");
        System.out.println("1 - Consulta saldo");
        System.out.println("2 - Depositar");
        System.out.println("3 - Sacar");
        System.out.println("4 - Informações cliente");
        System.out.println("0 - Parar");
        System.out.print("Digite uma opção: ");

    } 
}
