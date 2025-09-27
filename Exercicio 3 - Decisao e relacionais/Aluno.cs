using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace calculaNota
{
	public class Program
	{
		public static void Main(string[] args)
		{
			Console.WriteLine("Informe a nota");
			
			//Pede o input de nota
			string entradaNota = Console.ReadLine();
			float nota = float.Parse(entradaNota);
			
			//Logica
			if (nota <= 5) {
			  Console.WriteLine("Reprovado!");
			}else if (nota <= 6 && nota > 5) {
			  Console.WriteLine("Recuperação!");
			}else{
			  Console.WriteLine("Aprovado");
			}
		}
	}
}