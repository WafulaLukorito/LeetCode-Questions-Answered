
// """Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

// If target is not found in the array, return [-1, -1].

// You must write an algorithm with O(log n) runtime complexity.

//  """

import java.util.Arrays;

public class FirstAndLast{
    public static int bounds(int[] nums, int num, boolean isFirst){
       int index = -1, left= 0, right = nums.length -1;

       while (left <= right){
        int mid = left + (right - left)/2;

        if (nums[mid] == num){
            index = mid;

            if (isFirst){
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else if (nums[mid] > num){
            right = mid -1;
        } else {
            left = mid + 1;
        }
       }
return index;
}

public static int[] firstLast (int[] nums, int num){

    int[] firstLast = new int[2];
    firstLast[0] = bounds(nums, num, true);
    firstLast[1] = bounds(nums, num, false);

    return firstLast;
}

public static void main(String[] args) {
     int[] nums = {5, 7, 7, 8, 8, 10};
        int target = 8;
        System.out.println("Target range: " + Arrays.toString(firstLast(nums, target))); // Expected: [3, 4]
}

}