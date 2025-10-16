#include <stdio.h>

int main() {
    int idade;
    
    printf("Digite sua idade: ");
    scanf("%d", &idade);

    if (idade >= 18) {
        printf("Voce e maior de idade.\n");
    } else if (idade >= 12) {
        printf("Voce e um adolescente.\n");
    } else {
        printf("Voce e uma crianca.\n");
    }

    return 0;
}