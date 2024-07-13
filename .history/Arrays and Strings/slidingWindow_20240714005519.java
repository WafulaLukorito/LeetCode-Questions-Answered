
/*
 * Sliding Window
 * 1. Maximum Sum Subarray of Size K (easy)
 * 
 * Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
 * 
 */

public class slidingWindow {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6};
        int k = 3;
        System.out.println(findMaxSumSubArray(k, arr)); // 15
    }

    public static int findMaxSumSubArray(int k, int[] arr){

       // Input validation 
    if (arr.length <k){
        throw new IllegalArgumentException("Invalid input: Array must be longer than K")
    }

    // Compute sum of first window

    int maxSum = 0;
    for (int i = 0; i < k; i++){
        maxSum += arr[i];
    }

    //sum of remaining windows
    int windowSum = maxSum;
    for (int i =k; i<arr.length; i++){
        windowSum += arr[i] - arr[i - k];
        maxSum = Math.max(maxSum, windowSum);
    }
    return maxSum;
    }
}

// public class slidingWindow {
//     public static int findMaxSumSubArray(int k, int[] arr) {
//         int maxSum = 0;
//         int windowSum = 0;
//         int windowStart = 0;

//         for (int windowEnd = 0; windowEnd < arr.length; windowEnd++) {
//             windowSum += arr[windowEnd];

//             if (windowEnd >= k - 1) {
//                 maxSum = Math.max(maxSum, windowSum);
//                 windowSum -= arr[windowStart];
//                 windowStart++;
//             }
//         }

//         return maxSum;
//     }

//     public static void main(String[] args) {
//         int[] arr = { 2, 1, 5, 1, 3, 2 };
//         int k = 3;
//         System.out.println(findMaxSumSubArray(k, arr));
//     }
// }