import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] numbers = new int[N];

        for (int i = 0; i < N; i++) {
            numbers[i] = sc.nextInt();
        }

        Arrays.sort(numbers);

        long sum = 0;

        int start = N - 1;
        for (; start > 0; start -= 2) {
            if (numbers[start] <= 0 || numbers[start - 1] <= 0) {
                break;
            }
            sum += (long) numbers[start] * numbers[start - 1];
        }

        int end = 0;
        for (; end < start; end += 2) {
            if (numbers[end] < 1 && numbers[end + 1] < 1) {
                break;
            }
            sum += (long) numbers[end] * numbers[end + 1];
        }

        for (; end <= start; end++) {
            sum += numbers[end];
        }

        System.out.println(sum);
    }
}
