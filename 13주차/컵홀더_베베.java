import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        String seats = sc.next();

        int count = 1;
        int coupleSeats = 0;

        for (int i = 0; i < N; i++) {
            if (seats.charAt(i) == 'S') {
                count++;
            } else {
                coupleSeats++;
                i++;
            }
        }

        if (coupleSeats > 0) {
            count += coupleSeats;
        }

        System.out.println(count);
    }
}
