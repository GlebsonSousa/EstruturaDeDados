import java.util.Scanner;

public class Senha {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String senhaCorreta = "1234";
        String senhaUsuario = "";

        // Laço while que continua enquanto a senha estiver incorreta
        while (!senhaUsuario.equals(senhaCorreta)) {
            System.out.print("Digite a senha: ");
            senhaUsuario = scanner.nextLine();

            if (!senhaUsuario.equals(senhaCorreta)) {
                System.out.println("Senha incorreta!");
            }
        }

        System.out.println("Senha correta!");
        scanner.close();
    }
}
