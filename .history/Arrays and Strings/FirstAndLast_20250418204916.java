
// """Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

// If target is not found in the array, return [-1, -1].

// You must write an algorithm with O(log n) runtime complexity.

//  """

public class FirstAndLast{
    public static int bounds(int[] nums, int num, boolean isFirst){
        int left = 0, right = nums.length-1;
        int [] firstLast = new int[2];

       

        while (left < right){
             int mid = left + (right - left)/2;

        if (nums[mid] == num){
            if (isFirst == true){
                if (nums[mid - 1] != num
            }

        }
    }

    }
}