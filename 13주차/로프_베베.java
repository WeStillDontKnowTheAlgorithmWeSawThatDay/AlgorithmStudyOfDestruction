import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] ropes = new int[N];

        for (int i = 0; i < N; i++) {
            ropes[i] = sc.nextInt();
        }

        Arrays.sort(ropes);

        int maxWeight = 0;
        for (int i = 0; i < N; i++) {
            int weight = ropes[i] * (N - i);
            maxWeight = Math.max(maxWeight, weight);
        }

        System.out.println(maxWeight);
    }
}
