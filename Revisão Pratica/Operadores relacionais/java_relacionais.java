import java.util.Scanner;

public class java_relacionais {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite o primeiro valor: ");
        int a = scanner.nextInt();
        
        System.out.print("Digite o segundo valor: ");
        int b = scanner.nextInt();

        System.out.println("\nResultados:");
        System.out.println("a > b: " + (a > b));
        System.out.println("a < b: " + (a < b));
        System.out.println("a >= b: " + (a >= b));
        System.out.println("a <= b: " + (a <= b));
        System.out.println("a == b: " + (a == b));
        System.out.println("a != b: " + (a != b));

        scanner.close();
    }
}