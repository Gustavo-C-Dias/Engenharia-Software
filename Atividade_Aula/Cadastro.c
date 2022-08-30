#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main(){

    char nome[30], pais[30];
    int idade;

    printf("Informe seu nome: ");
    scanf("%s", &nome);

    printf("Informe sua idade: ");
    scanf("%d", &idade);

    printf("Informe seu pais: ");
    scanf("%s", &pais);

    printf("\n\nOlá %s, seu endereco %s foi cadastrado com sucesso", nome, pais);
}
    

