#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int tamanho;
    char matriz_texto[100][80];
    char linha[80];

    scanf("%d", &tamanho);

    fgets(linha, 80, stdin);
    fgets(linha, 80, stdin);

    int indice_matriz = 0;

    while (indice_matriz <= 100)
    {
        fgets(linha, 80, stdin);
        if (strcmp(linha, matriz_texto[indice_matriz - 1]) == 1)
        {
            fgets(linha, 80, stdin);
            strcpy(matriz_texto[indice_matriz], linha);
            indice_matriz++;
            printf("%d \n, %s", indice_matriz, linha);
            break;
        }
        strcpy(matriz_texto[indice_matriz], linha);
        indice_matriz++;
    }

    // imprimir matriz_texto
    for (int i = 0; i <= indice_matriz; i++)
    {
        //printf("%s", matriz_texto[i]);
    }

    char alfabeto[26] = "abcdefghijklmnopqrstuvwxyz";

    for (int i = 0; i <= indice_matriz; i++)
    {
        strcpy(linha, matriz_texto[i]);

        if (strlen(linha) == 44)
        {
            // verificar se linha tem todas as letras do alfabeto

            for (int j = 0; j < 26; j++)
            {

                if (strchr(linha, alfabeto[j]) == NULL)
                {
                    //printf("%s", linha);
                }
            }
        }
    }

    return 0;
}