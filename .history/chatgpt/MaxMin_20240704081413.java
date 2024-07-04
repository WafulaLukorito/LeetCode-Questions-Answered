
/* 
Given an array of integers, find the maximum and minimum of the array.

Example 1:
Input: [3, 5, 1, 2, 4, 8]
Output: Maximum: 8, Minimum: 1

Example 2:
Input: [1]
Output: Maximum: 1, Minimum: 1
*/


public class MaxMin{

    public static void main(String[] args) {
        int [] myArr = {1,2,5,8,-6};
        String res = minAndMax(myArr);
        System.out.println(res);
    }
    public String minAndMax(int[] arr){
        int n = arr.length;
        if (n < 1){
            return ("Invalid or empty Array");
        } else{

        int minVal = arr[0];
        int maxVal = arr[0];

        for (int i = 1; i <n; i++){
            if (arr[i] > maxVal){
                maxVal = arr[i];
            }
            if (arr[i] < minVal){
                minVal = arr[i]
            }
        }
        return ("Maximum: "+maxVal + ", Minimum: "+ minVal);

    }
}
}