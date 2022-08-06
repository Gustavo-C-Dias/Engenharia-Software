#include <stdio.h>

void main (){
    float nota1, nota2, media_final;

    printf("Informe a 1º nota: ");
    scanf("%f", &nota1);

    printf("Informe a 2º nota: ");
    scanf("%f", &nota2);

    media_final = (nota1 + nota2)/2;

    printf("A media final foi %.2f", media_final);
}