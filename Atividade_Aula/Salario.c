#include <stdio.h>

void main (){

    float salario_bruto, inss, ir, salario_liquido;

    printf("Informe o valor do seu salario_bruto: R$ ");
    scanf("%f", &salario_bruto);
    
    if (salario_bruto <= 1693.72){
        inss = salario_bruto * 0.08;
    } else if (salario_bruto >= 1693.72 && salario_bruto <= 2822.90){
        inss = salario_bruto * 0.09;
    } else if (salario_bruto >= 2822.91 && salario_bruto <= 5656.80){
        inss = salario_bruto * 0.11;
    } else {
        inss = 621.04;
    }

    if (salario_bruto >= 1903.98 && salario_bruto <= 2826.65){
        ir = salario_bruto * 0.075;
    } else if (salario_bruto >= 2826.66 && salario_bruto <= 3751.05){
        ir = salario_bruto * 0.15;
    } else if (salario_bruto >= 3751.06 && salario_bruto <= 4664.68){
        ir = salario_bruto * 0.225;
    } else if (salario_bruto >= 4664.68){
        ir = salario_bruto * 0.275;
    }

    salario_liquido = salario_bruto - inss - ir;

    printf(" Salario bruto = %2.f \n Salario liquido = %2.f \n Desconto INSS = %2.f \n Desconto do IR = %2.f", 
            salario_bruto, salario_liquido, inss, ir);
}