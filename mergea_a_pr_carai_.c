#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char dicionario_alfabeto[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

int find_in_array(char r)
{
    int j = 0;
    while (j < 26 && r != dicionario_alfabeto[j])
    {
        j++;
    }

    return j;
}

int find_n_array(char r, char array[80])
{
    int j = 0;
    while (j < 80 && r != array[j])
    {
        j++;
    }

    return j;
}

char *acha_alfabeto_linha(char linha[80])
{
    int j = 0, i = 0;
    char *achado = malloc(80 * sizeof(char));
    while (j < strlen(linha) && find_n_array(dicionario_alfabeto[j], linha) < 80)
    {
        //printf("%c", linha[j]);
        j++;
        achado[i] = linha[j];
        i++;
    }

    return achado;
}

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
            break;
        }
        strcpy(matriz_texto[indice_matriz], linha);
        indice_matriz++;
    }

    for (int i = 0; i <= indice_matriz; i++)
    {
        strcpy(linha, matriz_texto[i]);

        if (strlen(linha) == 44)
        {
            for (int i = 0; i < strlen(linha); i++)
            {
                if (linha[i] != ' ')
                {
                    printf("\n%s", acha_alfabeto_linha(linha));
                }
            }
        }
    }

    return 0;
}
