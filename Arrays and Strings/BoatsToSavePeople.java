// # * You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

// # *Return the minimum number of boats to carry every given person.

import java.util.Arrays;

public class BoatsToSavePeople {

    public static int boatsToSavePeople(int[] people, int limit) {
        Arrays.sort(people); // O(n log n). unlike pythoon, java does not have a built in sort method for
                             // arrays of primitive types, so we have to use the Arrays.sort() method which
                             // uses a dual-pivot quicksort algorithm and has an average time complexity of
                             // O(n log n).
        int left = 0;
        int right = people.length - 1;
        int boats = 0;

        while (left <= right) {
            if (people[left] + people[right] <= limit) {
                left++;
            }
            right--;
            boats++;
        }
        return boats;
    }

    public static void main(String[] args) {
        int[] people = { 3, 2, 2, 1 };
        int limit = 3;
        System.out.println("Minimum boats needed: " + boatsToSavePeople(people, limit));
    }
}
