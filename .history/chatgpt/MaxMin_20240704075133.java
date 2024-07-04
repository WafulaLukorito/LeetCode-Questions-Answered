
/* 
Given an array of integers, find the maximum and minimum of the array.

Example 1:
Input: [3, 5, 1, 2, 4, 8]
Output: Maximum: 8, Minimum: 1

Example 2:
Input: [1]
Output: Maximum: 1, Minimum: 1
*/


public class MaxMin {

    public static void main (String[] args){
        int[] my_arr = {1,2,3,5};
        String res = min_and_max(my_arr);
        System.out.println(res);
    }
 public static String min_and_max (int[] arr )  {
    n = arr.length();
    if (n < 1){
        return "Empty or invalid array";
    } else {
        max_val = arr[0];
        min_val = arr[0];

        for  (int i, arr, i++){
            if (arr[i] > max_val){
                max_val = arr[i];
            }
            if (arr[i] < min_val){
                min_val = arr[i];
            }
        }
    }
    return ("Maximum: " + max_val + ", minimum: "+min_val);

 }
}