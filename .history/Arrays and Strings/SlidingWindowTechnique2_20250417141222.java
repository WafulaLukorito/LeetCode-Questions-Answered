
// *Given an array of integers of size N, find maximum sum of K consecutive elements.

import java.util.Scanner;

public class SlidingWindowTechnique2{

    public static int maxSumSubArray (int[] nums, int k){
        if (k < nums.length){
            throw new IllegalArgumentException("Invlid array!");
        } else {
            int windowSum, maxSum = 0;
            //first K elements
            for (int i=0; i<k; i++){
                windowSum += nums[i];
            }
            maxSum = windowSum;

            //Slide the Window
            for (int i=k; i<nums.length; i++){
                windowSum += nums[i] - nums[i-k];
                maxSum = Math.max(windowSum, maxSum);
            }
            return maxSum;
        }
    }

    public static void main (String[] args){
        int[] nums = {1,2,3,4,5,6,7,8,9};
        Scanner input = new Scanner(System.in);
        System.out.println("Input desired window size:");
        int element = input.nextInt();
        int res = maxSumSubArray(nums, element);
        System.out.println("The max sum for window "+ element + " is "+res+".");
    }
}