#include <iostream>
using namespace std;

int main() 

{
  float valorCompra;

  cout << "Digite o valor da compra:";
  cin >> valorCompra;
  
  if(valorCompra >= 100.0)
  {
    cout << "Frete grátis " << "O valor da compra é: R$"<< valorCompra ;
  }
  else {
    valorCompra += 15.0;
    cout << "Frete adicionado! " <<"O valor da compra é: R$"<< valorCompra;
  }
  
}