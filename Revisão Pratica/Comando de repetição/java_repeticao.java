import java.util.Scanner;

public class java_repeticao {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite um numero para o fim da contagem: ");
        int limite = scanner.nextInt();
        
        for (int i = 1; i <= limite; i++) {
            System.out.println("Numero: " + i);
        }
        
        scanner.close();
    }
}