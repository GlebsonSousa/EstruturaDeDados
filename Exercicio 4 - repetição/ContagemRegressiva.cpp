#include <iostream>
using namespace std;

int main() 
{
  int numero;
  
  
    cout << "Digite um número inteiro positivo: ";
    cin >> numero;
    
    if (numero < 0)
    {
      cout << "Digite um valor válido!!!!!!";
    }
    
    else
    {
      
      while (numero>=0)
      {
        cout << numero << endl; 
        numero --;
      }
    
      cout << "Fim da contagem" << endl;
    }

}