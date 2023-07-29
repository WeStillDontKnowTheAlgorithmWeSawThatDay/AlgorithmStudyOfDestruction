package org.example;

import java.io.*;
import java.util.*;

import static java.lang.Integer.parseInt;
import static java.util.Collections.sort;

public class Main {

    public static void main(String[] args) throws IOException {
        final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        final String fakeInput = reader.readLine();
        final StringTokenizer user1InputStringTokenizer = new StringTokenizer(reader.readLine(), " ");
        final List<Integer> user1HadNumbers = new ArrayList<>();

        while (user1InputStringTokenizer.hasMoreTokens()) {
            final int user1InputCount = parseInt(user1InputStringTokenizer.nextToken());
            user1HadNumbers.add(user1InputCount);
        }
        sort(user1HadNumbers);

        final List<Integer> responses = new ArrayList<>();
        final String fakeInput2 = reader.readLine();
        final StringTokenizer user2InputStringTokenizer = new StringTokenizer(reader.readLine(), " ");

        while (user2InputStringTokenizer.hasMoreTokens()) {
            final int target = parseInt(user2InputStringTokenizer.nextToken());
            if (isContainTarget(user1HadNumbers, target)) {
                responses.add(1);
            } else {
                responses.add(0);
            }
        }

        for (final int response : responses) {
            System.out.print(response + " ");
        }

    }

    private static boolean isContainTarget(final List<Integer> user1HadNumbers, final int target) {
        int leftIndex = 0;
        int rightIndex = user1HadNumbers.size() - 1;

        while (leftIndex <= rightIndex) {
            final int midIndex = (leftIndex + rightIndex) / 2;
            final int midIndexValue = user1HadNumbers.get(midIndex);
            if (midIndexValue == target) {
                return true;
            } else if (midIndexValue < target) {
                leftIndex = midIndex + 1;
            } else if (target < midIndexValue) {
                rightIndex = midIndex - 1;
            }
        }
        return false;
    }

}
