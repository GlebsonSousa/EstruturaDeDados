#include <iostream>

int main() {
    int idade;
    
    std::cout << "Digite sua idade: ";
    std::cin >> idade;

    if (idade >= 18) {
        std::cout << "Voce e maior de idade." << std::endl;
    } else if (idade >= 12) {
        std::cout << "Voce e um adolescente." << std::endl;
    } else {
        std::cout << "Voce e uma crianca." << std::endl;
    }

    return 0;
}