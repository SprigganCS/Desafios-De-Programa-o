#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *acha_frase(char *linha) // função que encontra frase chave (tamanho 44 e possui todas as letras do alfabeto)
{
    char alfabeto[26] = "abcdefghijklmnopqrstuvwxyz";
    int cont = 0;
    int i;
    for (i = 0; i < 26; i++)
    {
        if (strchr(linha, alfabeto[i]) == NULL)
        {
            break;
        }
    }
    if (i == 26)
    {
        // printf("%s", linha); // printa a chave
        return linha;
    }
    else
    {
        return "";
    }
}

char *cria_alfabeto(char *chave, char *alfabeto_novo)
{
    chave[17] = ' ';
    chave[21] = ' ';
    chave[26] = ' ';
    chave[28] = ' ';
    chave[29] = ' ';
    chave[31] = ' ';
    chave[32] = ' ';
    chave[33] = ' ';
    chave[41] = ' ';

    char chave_tratada[26];
    int j = 0;
    for (int i = 0; i < 43; i++)
    { // removendo espaços da chave e preenchendo chave_tratada
        if (chave[i] != ' ')
        {
            chave_tratada[j] = chave[i];
            j++;
        }
    }
    // printf("%s\n", chave_tratada);

    // int vet[35] = {19, 7, 4, 16, 20, 8, 2, 10, 1, 17, 14, 22, 13, 5, 14, 23, 9, 20, 12, 15, 18, 14, 21, 4, 17, 19, 7, 4, 11, 0, 25, 24, 3, 14, 6};
    int vet[26] = {19, 7, 4, 16, 20, 8, 2, 10, 1, 17, 14, 22, 13, 5, 23, 9, 12, 15, 18, 21, 11, 0, 25, 24, 3, 6};
    for (int i = 0; i < 26; i++)
    {
        alfabeto_novo[vet[i]] = chave_tratada[i];
        // printf("%d ", vet[i]);
    }
    // printf("%s", alfabeto_novo); //ler somente até a posição 26

    return alfabeto_novo;
}

char traduz(char *tradutor, char *matriz_texto)
{
    char alfabeto[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
    int j;
    for (int i = 0; i < strlen(matriz_texto); i++)
    {
        char aux = matriz_texto[i];
        for (j = 0; j < 26; j++)
        {
            if (aux == tradutor[j])
            {
                break;
            }
        }
        if (j == 26)
        {
            printf(" ");
        }
        else
        {
            printf("%c", alfabeto[j]);
        }
    }
    printf("\n");
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

    // imprimir matriz_texto
    for (int i = 0; i <= indice_matriz; i++)
    {
        // printf("%s", matriz_texto[i]);
    }

    char alfabeto[26] = "abcdefghijklmnopqrstuvwxyz";
    char *chave;
    for (int i = 0; i <= indice_matriz; i++)
    {
        strcpy(linha, matriz_texto[i]);

        if (strlen(linha) == 44)
        { // entra no if se a frase tem o tamanho da chave
          // deve verificar se linha tem todas as letras do alfabeto (se realmente é a chave)
            chave = acha_frase(linha);
            // printf("%s\n", chave);
            if (strlen(chave) == 44)
            {
                // /printf("%s\n", chave);
                break;
            }
        }
    }
    if (strlen(chave) != 44)
    {
        printf("No solution");
        return 0;
    }

    char aux[26];
    char *tradutor;
    tradutor = cria_alfabeto(chave, aux);

    for (int i = 0; i < indice_matriz; i++)
    {
        traduz(tradutor, matriz_texto[i]);
    }

    return 0;
}
