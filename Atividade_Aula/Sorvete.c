#include <stdio.h>
#include <string.h>

main (){

    int codigo = 0;

    do {
        printf("1 - Flocos \n");
        printf("2 - Morango \n");
        printf("3 - Napolitano \n");
        printf("4 - Banana \n");
        printf("5 - Leite Ninho \n");
        printf(" Informe o sabor de sorvete desejado: ");
        scanf("%i", &codigo);

        switch (codigo){

            case 1:
                printf("\n\nTabela Nutricional Sorvete de Flocos \n");
                printf("   Um monte de dados ...\n\n");
                break;
            
            case 2:
                printf("\n\nTabela Nutricional Sorvete de Morango \n");
                printf("   Um monte de dados ... \n\n");
                break;

            case 3:
                printf("\n\nTabela Nutricional Sorvete de Napolitano \n");
                printf("   Um monte de dados ... \n\n");
                break;

            case 4:
                printf("\n\nTabela Nutricional Sorvete de Banana \n");
                printf("   Um monte de dados ... \n\n\n");
                break;
            
            case 5:
                printf("\n\nTabela Nutricional Sorvete de Leite Ninho \n");
                printf("   Um monte de dados ... \n\n");
                break;

            default:
                printf("Esse sabor não temos, inicie uma outra busca \n\n");
                break;
        }

    } while (codigo >= 1 && codigo <= 5);

}