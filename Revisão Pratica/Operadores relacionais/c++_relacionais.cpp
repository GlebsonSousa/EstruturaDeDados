#include <iostream>

int main() {
    int a, b;

    std::cout << "Digite o primeiro valor: ";
    std::cin >> a;
    
    std::cout << "Digite o segundo valor: ";
    std::cin >> b;

    std::cout << std::boolalpha;
    std::cout << "\nResultados:" << std::endl;
    std::cout << "a > b: " << (a > b) << std::endl;
    std::cout << "a < b: " << (a < b) << std::endl;
    std::cout << "a >= b: " << (a >= b) << std::endl;
    std::cout << "a <= b: " << (a <= b) << std::endl;
    std::cout << "a == b: " << (a == b) << std::endl;
    std::cout << "a != b: " << (a != b) << std::endl;

    return 0;
}