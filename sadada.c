#include <stdio.h>
#include <stdlib.h>

void printaMat(int *mat){ //printa a matriz
    int i, j;
    for(i=0; i<8; i++){
        for(j=0; j<8; j++){
            printf("%d ", mat[i*8+j]);
        }
        printf("\n");
    }
}

struct RegistroMovimentos{ //estrutura para guardar os movimentos
    int M;
    int pos;
};

int movimento(int x, int *mat, struct RegistroMovimentos *movimentos, int i, int m) { //recebe a posição e movimenta //int i é quanto já preencheu, e m o ultimo movimento feito (começ
    printf("%d %d %d\n", x, i, m);
    
    if(mat[x-8+2]==-1 && m<1){ //"se o movimento 1 for permitido"
        mat[x-8+2]=i; //preenche a posição
        movimentos[i].M=1; //registra o movimento
        movimentos[i].pos=x-8+2; //registra a posição
        i++;
        movimento(x-8+2, mat, movimentos, i, 0); //chamada recursiva
    }

    else if (mat[x-16+1]==-1 && m<2 ){  //"se o movimento 2 for permitido"
        mat[x-16+1]=i;
        movimentos[i].M=2;
        movimentos[i].pos=x-16+1;
        i++;
        movimento(x-16+1, mat, movimentos, i, 0);

    }else if(mat[x-16-1]==-1 && m<3){ //"se o movimento 3 for permitido"
        mat[x-16-1]=i;
        movimentos[i].M=3;
        movimentos[i].pos=x-16-1;
        i++;
        movimento(x-16-1, mat, movimentos, i, 0);

    }else if(mat[x-8-2]==-1 && m<4){ //"se o movimento 4 for permitido"
        mat[x-8-2]=i;
        movimentos[i].M=4;
        movimentos[i].pos=x-8-2;
        i++;
        movimento(x-8-2, mat, movimentos, i, 0);

    }else if(mat[x+8-2]==-1 && m<5){ //"se o movimento 5 for permitido"
        //verificar se a posição x é possível de realizar o movimento +8-2 de forma correta
        mat[x+8-2]=i;
        movimentos[i].M=5;
        movimentos[i].pos=x+8-2;
        i++;
        movimento(x+8-2, mat, movimentos, i, 0);

    }else if(mat[x+16-1]==-1 && m<6){ //"se o movimento 6 for permitido"
        printf("foi");
        mat[x+16-1]=i;
        movimentos[i].M=6;
        movimentos[i].pos=x+16-1;
        i++;
        movimento(x+16-1, mat, movimentos, i, 0);

    }else if(mat[x+16+1]==-1 && m<7){ //"se o movimento 7 for permitido"
        mat[x+16+1]=i;
        movimentos[i].M=7;
        movimentos[i].pos=x+16+1;
        i++;
        movimento(x+16+1, mat, movimentos, i, 0);

    }else if(mat[x+8+2]==-1 && m<8){ //"se o movimento 8 for permitido"
        mat[x+8+2]=i;
        movimentos[i].M=8;
        movimentos[i].pos=x+8+2;
        i++;
        return 0;
        movimento(x+8+2, mat, movimentos, i, 0);
    }

    else{
        if(i==64) return 1; //se preencheu tudo, retorna 1
        i--;
        printf("entrou no else %d %d %d\n",movimentos[i].pos, i, movimentos[i].M);
        mat[movimentos[i].pos] = -1;
        movimento(movimentos[i].pos, mat, movimentos, i, movimentos[i].M);
        
    }

    
    
}

void passeio(int x, int y){ //recebe a posição inicial do cavalo
    int *mat = (int*) malloc(8*8*sizeof(int)); //cria a matriz
    int i, j;

    for(i=0; i<8; i++){ //inicializa a matriz com 0
        for(j=0; j<8; j++){
            mat[i*8+j] = -1;
        }
    }

    struct RegistroMovimentos *movimentos = (struct RegistroMovimentos*) malloc(64*sizeof(struct RegistroMovimentos)); //declara o vetor de movimentos
    for(int i=0; i<64; i++){
        movimentos[i].M = -1;
    }

    mat[(x - 1)*8+y - 1] = 1; //preenche a posição inicial com 1
    int teste = movimento((x - 1 * y), mat, movimentos, 1, 0); //chama a função de movimento
    if(teste == 1){
        printf("O passeio foi realizado com sucesso!\n");
        
        for(int i=0; i<64; i++){
            printf("%d ", movimentos[i].M);
        }
        printf("\n\n");
        printaMat(mat); //imprime a matriz
    }



}



int main(){
    passeio(1,1);
    return 0;
}
