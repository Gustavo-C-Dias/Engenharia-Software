package com.mycompany.sistemabancario;

public class Contas {
    private int conta;
    private double saldo;
    private Clientes cliente;

    public Contas (int conta, Clientes cliente){
        this.conta = conta;
        this.saldo = 0;
        this.cliente = cliente;
    }
    
    public Clientes getCliente(){
        return this.cliente;
    }
    
    public double getSaldo(){ 
        return this.saldo;
    }
    
    public void depositar(double valorDeposito){
        if (valorDeposito > 0) {
            this.saldo += valorDeposito;
            System.out.println("Deposito realizado");
        } else {
            System.out.println("Informe um valor valído");
        }
    }
    
    public void sacar(double valorSaque){
        if (valorSaque > 0) {
            if (this.saldo - valorSaque >= 0){
                this.saldo -= valorSaque;
                System.out.println("Saque realizado");
            } else {
                System.out.println("Saldo insuficiente");
            }
        } else {
            System.out.println("Informe um valor valido");
        }
    }
}
