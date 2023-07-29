import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        boolean[][] board = new boolean[100][100];
        int count = 0;

        for (int i = 0; i < N; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();

            for (int j = x; j < x + 10; j++) {
                for (int k = y; k < y + 10; k++) {
                    if (!board[j][k]) {
                        board[j][k] = true;
                        count++;
                    }
                }
            }
        }

        System.out.println(count);
    }
}
