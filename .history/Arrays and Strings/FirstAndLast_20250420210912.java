
// """Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

// If target is not found in the array, return [-1, -1].

// You must write an algorithm with O(log n) runtime complexity.

//  """

public class FirstAndLast{
    public static int[] bounds(int[] nums, int num, boolean isFirst){

        int left = 0;
        int right = nums.length - 1;

        while (left <= right){
            int mid = left + (right - left)/2;

            if (isFirst){
                if (nums[mid]==num && (nums[mid-1] != num || mid == 0)){
                    return mid;
                } else {
                    right = mid - 1;
                }
            } else {
                if (nums[mid] ==num && (nums[mid+1] != num || mid == nums.length -1)){
                    return mid;
                } else {
                    left = mid + 1;
                }
            }
        }

        return -1;

    }
}