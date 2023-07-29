import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[][] board = new int[5][5];
        HashMap<Integer, Point> targetMap = new HashMap<>();
        int targetCount = 0;

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                board[i][j] = sc.nextInt();
                targetMap.put(board[i][j], new Point(i, j));
            }
        }

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                targetCount++;
                int num = sc.nextInt();
                Point point = targetMap.get(num);
                board[point.x][point.y] = 0;
                if (isBingo(board)) {
                    System.out.println(targetCount);
                    return;
                }
            }
        }
    }

    public static boolean isBingo(int[][] board) {
        int bingoCount = 0;

        for (int i = 0; i < 5; i++) {
            if (board[i][0] == 0 && board[i][1] == 0 && board[i][2] == 0 && board[i][3] == 0 && board[i][4] == 0) {
                bingoCount++;
            }
        }

        for (int i = 0; i < 5; i++) {
            if (board[0][i] == 0 && board[1][i] == 0 && board[2][i] == 0 && board[3][i] == 0 && board[4][i] == 0) {
                bingoCount++;
            }
        }

        if (board[0][0] == 0 && board[1][1] == 0 && board[2][2] == 0 && board[3][3] == 0 && board[4][4] == 0) {
            bingoCount++;
        }
        if (board[0][4] == 0 && board[1][3] == 0 && board[2][2] == 0 && board[3][1] == 0 && board[4][0] == 0) {
            bingoCount++;
        }

        return bingoCount >= 3;
    }

    static class Point {
        int x, y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
