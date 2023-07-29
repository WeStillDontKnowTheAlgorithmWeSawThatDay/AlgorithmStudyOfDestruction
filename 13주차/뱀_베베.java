import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Point {
    int x, y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    public static int N, K, L;
    public static int[][] board;
    public static int[] dx = {0, 1, 0, -1};
    public static int[] dy = {1, 0, -1, 0};
    public static int direction = 0;
    public static Queue<Point> snake = new LinkedList<>();
    public static Queue<Command> commands = new LinkedList<>();

    static class Command {
        int time;
        char dir;

        Command(int time, char dir) {
            this.time = time;
            this.dir = dir;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        K = sc.nextInt();
        board = new int[N][N];

        for (int i = 0; i < K; i++) {
            int row = sc.nextInt() - 1;
            int col = sc.nextInt() - 1;
            board[row][col] = 1;
        }

        L = sc.nextInt();

        for (int i = 0; i < L; i++) {
            int time = sc.nextInt();
            char dir = sc.next().charAt(0);
            commands.add(new Command(time, dir));
        }

        int time = 0;
        int headX = 0, headY = 0;
        snake.add(new Point(headX, headY));

        while (true) {
            time++;

            headX += dx[direction];
            headY += dy[direction];

            if (headX < 0 || headY < 0 || headX >= N || headY >= N || isCollision(headX, headY)) {
                break;
            }

            snake.add(new Point(headX, headY));

            if (board[headX][headY] == 1) {
                board[headX][headY] = 0;
            } else {
                snake.poll();
            }

            if (!commands.isEmpty() && commands.peek().time == time) {
                Command cmd = commands.poll();
                if (cmd.dir == 'L') {
                    direction = (direction + 3) % 4;
                } else {
                    direction = (direction + 1) % 4;
                }
            }
        }

        System.out.println(time);
    }

    public static boolean isCollision(int x, int y) {
        for (Point p : snake) {
            if (p.x == x && p.y == y) {
                return true;
            }
        }
        return false;
    }
}
