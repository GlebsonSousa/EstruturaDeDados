using System;

class Repeticao {
    static void Main() {
        Console.Write("Digite um numero para o fim da contagem: ");
        int limite = Convert.ToInt32(Console.ReadLine());
        
        for (int i = 1; i <= limite; i++) {
            Console.WriteLine($"Numero: {i}");
        }
    }
}