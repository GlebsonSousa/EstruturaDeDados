using System;

class Aritmeticos {
    static void Main() {
        Console.Write("Digite o primeiro numero: ");
        int num1 = Convert.ToInt32(Console.ReadLine());

        Console.Write("Digite o segundo numero: ");
        int num2 = Convert.ToInt32(Console.ReadLine());

        int soma = num1 + num2;
        int sub = num1 - num2;
        int mult = num1 * num2;
        double div = (double)num1 / num2;

        Console.WriteLine("\nResultados:");
        Console.WriteLine($"Soma: {soma}");
        Console.WriteLine($"Subtracao: {sub}");
        Console.WriteLine($"Multiplicacao: {mult}");
        Console.WriteLine($"Divisao: {div}");
    }
}