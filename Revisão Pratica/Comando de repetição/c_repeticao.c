#include <stdio.h>

int main() {
    int limite;
    
    printf("Digite um numero para o fim da contagem: ");
    scanf("%d", &limite);

    for (int i = 1; i <= limite; i++) {
        printf("Numero: %d\n", i);
    }
    
    return 0;
}