/*
	Alunos: Arthur Rodrigues Proença, André Neves Medeiros e Tiago Soares
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int linhas, colunas;
char numero[23][12];
char numeros[8][23][12];

void mostra_linha(int linha_indice)
{
	for (int j = 1; j < colunas - 1; j++)
	{
		numero[linha_indice][j] = 45;
	}
}

void mostra_prim_coluna(int coluna_indice)
{
	for (int i = 1; i < linhas/2; i++)
	{
		numero[i][coluna_indice] = 124;
	}
}

void mostra_ult_coluna(int coluna_indice)
{
	for (int i = (linhas / 2) + 1; i < linhas - 1; i++)
	{
		numero[i][coluna_indice] = 124;
	}
}

void primeira_linha()
{
	mostra_linha(0);
}

void meia_linha()
{
	mostra_linha(linhas / 2);
}

void ultima_linha()
{
	mostra_linha(linhas - 1);
}

void primeira_coluna_esq()
{
	mostra_prim_coluna(0);
}

void primeira_coluna_dir()
{
	mostra_prim_coluna(colunas - 1);
}

void ultima_coluna_esq()
{
	mostra_ult_coluna(0);
}

void ultima_coluna_dir()
{
	mostra_ult_coluna(colunas - 1);
}

void mostra_numero(int numero_indice)
{
	for (int i = 0; i < linhas; i++)
	{
		for (int j = 0; j < colunas; j++)
		{
			numeros[numero_indice][i][j] = numero[i][j];
		}
	}
}

void mostra_zero(int indice)
{
	for (int i = 0; i < linhas; i++)
	{
		int j;
		for (j = 0; j < colunas; j++)
		{
			numero[i][j] = ' ';
		}
	}
	primeira_linha();

	primeira_coluna_esq();
	primeira_coluna_dir();
	ultima_coluna_esq();
	ultima_coluna_dir();
	ultima_linha();
	mostra_numero(indice);
}

void mostra_um(int indice)
{
	for (int i = 0; i < linhas; i++)
	{
		int j;
		for (j = 0; j < colunas; j++)
		{
			numero[i][j] = ' ';
		}
	}
	primeira_coluna_dir();
	ultima_coluna_dir();
	mostra_numero(indice);
}

void mostra_dois(int indice)
{
	for (int i = 0; i < linhas; i++)
	{
		int j;
		for (j = 0; j < colunas; j++)
		{
			numero[i][j] = ' ';
		}
	}
	primeira_linha();
	primeira_coluna_dir();
	meia_linha();
	ultima_coluna_esq();
	ultima_linha();
	mostra_numero(indice);
}

void mostra_tres(int indice)
{
	for (int i = 0; i < linhas; i++)
	{
		int j;
		for (j = 0; j < colunas; j++)
		{
			numero[i][j] = ' ';
		}
	}
	primeira_linha();
	primeira_coluna_dir();
	meia_linha();
	ultima_coluna_dir();
	ultima_linha();
	mostra_numero(indice);
}

void mostra_quatro(int indice)
{
	for (int i = 0; i < linhas; i++)
	{
		int j;
		for (j = 0; j < colunas; j++)
		{
			numero[i][j] = ' ';
		}
	}
	primeira_coluna_esq();
	primeira_coluna_dir();
	meia_linha();
	ultima_coluna_dir();
	mostra_numero(indice);
}

void mostra_cinco(int indice)
{
	for (int i = 0; i < linhas; i++)
	{
		int j;
		for (j = 0; j < colunas; j++)
		{
			numero[i][j] = ' ';
		}
	}
	primeira_linha();
	primeira_coluna_esq();
	meia_linha();
	ultima_coluna_dir();
	ultima_linha();
	mostra_numero(indice);
}

void mostra_seis(int indice)
{
	for (int i = 0; i < linhas; i++)
	{
		int j;
		for (j = 0; j < colunas; j++)
		{
			numero[i][j] = ' ';
		}
	}
	primeira_linha();
	primeira_coluna_esq();
	meia_linha();
	ultima_coluna_esq();
	ultima_coluna_dir();
	ultima_linha();
	mostra_numero(indice);
}

void mostra_sete(int indice)
{
	for (int i = 0; i < linhas; i++)
	{
		int j;
		for (j = 0; j < colunas; j++)
		{
			numero[i][j] = ' ';
		}
	}
	primeira_linha();
	primeira_coluna_dir();
	ultima_coluna_dir();
	mostra_numero(indice);
}

void mostra_oito(int indice)
{
	for (int i = 0; i < linhas; i++)
	{
		int j;
		for (j = 0; j < colunas; j++)
		{
			numero[i][j] = ' ';
		}
	}
	primeira_linha();
	primeira_coluna_esq();
	primeira_coluna_dir();
	meia_linha();
	ultima_coluna_esq();
	ultima_coluna_dir();
	ultima_linha();
	mostra_numero(indice);
}

void mostra_nove(int indice)
{
	for (int i = 0; i < linhas; i++)
	{
		int j;
		for (j = 0; j < colunas; j++)
		{
			numero[i][j] = ' ';
		}
	}
	primeira_linha();
	primeira_coluna_esq();
	primeira_coluna_dir();
	meia_linha();
	ultima_coluna_dir();
	ultima_linha();
	mostra_numero(indice);
}

void mostra_numero_function(int n, int index)
{
	void (*function[10])(int index) = {mostra_zero, mostra_um, mostra_dois, mostra_tres, mostra_quatro, mostra_cinco, mostra_seis, mostra_sete, mostra_oito, mostra_nove};
	function[n](index);
}

void main()
{
	char numeros_[9];
	int tamanho;

	while (1)
	{
		int indice_numero = 0;

		scanf("%i %s", &tamanho, numeros_);

		if (tamanho == 0 && strcmp(numeros_, "0") == 0)
			break;

		linhas = (2 * tamanho) + 3;
		colunas = (tamanho + 2);

		for (int i = 0; i < strlen(numeros_); i++)
		{
			mostra_numero_function(numeros_[i] - '0', i);
		}
		int i, j, k;
		for (i = 0; i < linhas; i++)
		{
			for (j = 0; j < strlen(numeros_); j++)
			{
				for (k = 0; k < colunas; k++)
				{
					printf("%c", numeros[j][i][k]);
				}
				if (j < strlen(numeros_) - 1)
					printf(" ");
			}
			printf("\n");
		}
	}
}
