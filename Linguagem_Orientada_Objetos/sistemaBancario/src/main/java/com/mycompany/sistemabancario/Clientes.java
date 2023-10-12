package com.mycompany.sistemabancario;

public class Clientes {
    private String nome, sobrenome, cpf;
    
    Clientes(String nome, String sobrenome, String cpf){
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.cpf = cpf;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getSobrenome() {
        return sobrenome;
    }

    public void setSobrenome(String sobrenome) {
        this.sobrenome = sobrenome;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }
    
    @Override
    public String toString(){
        return ("Nome Completo: "+ this.nome + " " + this.sobrenome + "\n"
                + "CPF: " + this.cpf);
    }
}