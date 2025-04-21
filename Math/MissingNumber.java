
// """Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

// Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

// #? Use Gauss Formula

// #?Time Complexity O(n) as we loop over elements of array once

// #? Space complexity O(1)
//     """

import java.util.Arrays;

public class MissingNumber{
    public static int missingNumber(int[] nums){
     int n = nums.length;

     int intendedSum = n * (n+1)/2;

     int trueSum = Arrays.stream(nums).sum();

     return intendedSum - trueSum;
    }

    // Sorting and Linear Scan (O(n log n) time)

// Less efficient, but straightforward:

// java
// Arrays.sort(nums);
// for (int i = 0; i < nums.length; i++) {
//     if (nums[i] != i) return i;
// }
// return nums.length;

    public static void main(String[] args) {
        int[] nums = {9, 6, 4, 2, 3, 5, 7, 0, 1};
        System.out.println("The missing number: "+missingNumber(nums));
    }
}