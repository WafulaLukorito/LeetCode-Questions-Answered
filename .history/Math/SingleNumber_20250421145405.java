/*Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
 */

public class SingleNumber {
    public static int findSingle(int[] nums) {
        int result = 0;
        for (int num : nums) {
            result ^= num; // XOR all elements
        }
        return result;
    }

    public static void main(String[] args) {
        int[] nums = {4, 1, 2, 1, 2};
        System.out.println("Single number: " + findSingle(nums)); // Output: 4
    }
}

/*

import java.util.HashSet;
import java.util.Set;

public class SingleNumber {
    public static int singleNumberWithSet(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (seen.contains(num)) {
                seen.remove(num); // Duplicate found, remove it
            } else {
                seen.add(num); // New number, add to set
            }
        }
        // The remaining element is the single number
        return seen.iterator().next();
    }

    public static void main(String[] args) {
        int[] nums = {4, 1, 2, 1, 2};
        System.out.println("The single number (using set) is: " + singleNumberWithSet(nums)); // Output: 4
    }
}
*/

/* 
import java.util.HashSet;
import java.util.Set;

public class SingleNumber {
    public static int singleNumberWithSum(int[] nums) {
        Set<Integer> uniqueNums = new HashSet<>();
        int actualSum = 0;
        for (int num : nums) {
            uniqueNums.add(num); // Track unique numbers
            actualSum += num;    // Track total sum
        }
        // Intended sum if all appeared twice: 2 × sum_of_uniques
        int intendedSum = 0;
        for (int num : uniqueNums) {
            intendedSum += 2 * num;
        }
        // The single number is intendedSum - actualSum
        return intendedSum - actualSum;
    }

    public static void main(String[] args) {
        int[] nums = {4, 1, 2, 1, 2};
        System.out.println("The single number (using sum) is: " + singleNumberWithSum(nums)); // Output: 4
    }
}
    */