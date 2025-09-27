#include <stdio.h>

int main()
{

  int entrada;

  // Pede entrada ao usuario
  printf("Informe a sua idade:");

  scanf("%d", &entrada);

  printf("\n\n");

  if (entrada < 18)
  {
    printf("Você é menor de idade !!");
  }
  else
  {
    printf("Você é maior de idade !!");
  }
}