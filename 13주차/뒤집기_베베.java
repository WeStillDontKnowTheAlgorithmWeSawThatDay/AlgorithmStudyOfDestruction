import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String s = sc.next();

        int count0 = 0;
        int count1 = 0;

        if (s.charAt(0) == '0') {
            count0++;
        } else {
            count1++;
        }

        for (int i = 1; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            char prevChar = s.charAt(i - 1);

            if (currentChar != prevChar) {
                if (currentChar == '0') {
                    count0++;
                } else {
                    count1++;
                }
            }
        }

        int minFlips = Math.min(count0, count1);

        System.out.println(minFlips);
    }
}
