using System;

class Relacionais {
    static void Main() {
        Console.Write("Digite o primeiro valor: ");
        int a = Convert.ToInt32(Console.ReadLine());
        
        Console.Write("Digite o segundo valor: ");
        int b = Convert.ToInt32(Console.ReadLine());

        Console.WriteLine("\nResultados:");
        Console.WriteLine($"a > b: {a > b}");
        Console.WriteLine($"a < b: {a < b}");
        Console.WriteLine($"a >= b: {a >= b}");
        Console.WriteLine($"a <= b: {a <= b}");
        Console.WriteLine($"a == b: {a == b}");
        Console.WriteLine($"a != b: {a != b}");
    }
}