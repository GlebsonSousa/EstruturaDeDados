#include <iostream>

int main() {
    int limite;
    
    std::cout << "Digite um numero para o fim da contagem: ";
    std::cin >> limite;
    
    for (int i = 1; i <= limite; i++) {
        std::cout << "Numero: " << i << std::endl;
    }

    return 0;
}