using System;

class Decisao {
    static void Main() {
        Console.Write("Digite sua idade: ");
        int idade = Convert.ToInt32(Console.ReadLine());

        if (idade >= 18) {
            Console.WriteLine("Voce e maior de idade.");
        } else if (idade >= 12) {
            Console.WriteLine("Voce e um adolescente.");
        } else {
            Console.WriteLine("Voce e uma crianca.");
        }
    }
}