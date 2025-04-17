// """Given an array of integers arr, return true if and only if it is a valid mountain array.

// Recall that arr is a mountain array if and only if:

// arr.length >= 3
// There exists some i with 0 < i < arr.length - 1 such that:
// arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
// arr[i] > arr[i + 1] > ... > arr[arr.length - 1]


// #? Time Complexity = O(N)--- O(N)+O(N)---two loops over array

// #? Space Complexity = O(1) ---- did not use additional memory space

//     """

public class ValidMountainArray {

    public static boolean isValid(int[] nums){
        int n = nums.length;
        if (n < 3) return false;

        int i = 0;
        //climb
        // while (i < n-1 && nums[i]<nums[i+1]) i++;

        //Alow plateau
        while (i < n-1 && nums[i]<=nums[i+1]) i++;

        //check if we moved or got to end
        if (i==0 || i== n-1) return false;

        //go down
        // while (i < n-1 && nums[i]>nums[i+1]) i++;
        while (i < n-1 && nums[i]>=nums[i+1]) i++;

        //allow plateau


        return i == n-1;

    }

    public static void main(String[] args) {
        int[] arr1 = {2, 1}; // false
        int[] arr2 = {3, 5, 5,2}; // false
        int[] arr3 = {0, 3, 2, 1}; // true
        System.out.println(isValid(arr1)); // false
        System.out.println(isValid(arr2)); // false
        System.out.println(isValid(arr3)); // true
    }
}