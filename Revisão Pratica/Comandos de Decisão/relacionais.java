import java.util.Scanner;

public class java_decisao {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite sua idade: ");
        int idade = scanner.nextInt();

        if (idade >= 18) {
            System.out.println("Voce e maior de idade.");
        } else if (idade >= 12) {
            System.out.println("Voce e um adolescente.");
        } else {
            System.out.println("Voce e uma crianca.");
        }
        
        scanner.close();
    }
}