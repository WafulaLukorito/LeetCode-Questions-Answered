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

    public static Boolean isValid(int[] nums){
        if (nums.length < 3){
            return false;
        }

        //climb
        int i = 0;
        while (i < nums.length -1 && nums[i]<nums[i+1]){
            i++;
        }

        //check if we moved or we reached end
        if (i == 0 || i == nums.length -1) {
            return false;
        }

        //fall
        while (i < nums.length -1 && nums[i] > nums[i+1]){
            i++;
        }
        return i== nums.length -1;


    }

    public static void main(String[] args) {
        int[] arr1 = {2, 1}; // false
        int[] arr2 = {3, 5, 5}; // false
        int[] arr3 = {0, 3, 2, 1}; // true
        System.out.println(isValid(arr1)); // false
        System.out.println(isValid(arr2)); // false
        System.out.println(isValid(arr3)); // true
    }
}