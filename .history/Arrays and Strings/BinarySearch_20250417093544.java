

import java.util.Scanner;

public class BinarySearch{

    public static int binarySearch(int[] nums, int num){

        int left = 0, right = nums.length -1;

        while (right >= left){
            mid = left+ (right-left)/2;
            if (nums[mid] == num){
                return mid;
            }
            if (nums[mid] > num){
                right = mid -1;
            } else {
                left = mid +1;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        
        int [] nums = {1,2,3,4,5,6,7};

        Scanner input = new Scanner(System.in);
        System.out.println("Please enter number to search");
        int element = input.nextInt();

        int res = binarySearch(nums, element);

        if (res == -1){
            System.out.println("Element not found!");
        } else {
            System.out.println("Element found at index " + res);
        }
        input.close();
    }
}
















// public class BinarySearch{

//     public static void main(String[] args) {
//         int[] nums = {1,2,3,4,5,6,7};
//         int num = 5;
//         System.out.println(binarySearch(nums, num));
//     }

//     public static int binarySearch(int[] nums, int num){
//         int n = nums.length;
//         if (n < 1){
//             return -1;
//         } else {
//             int left = 0;
//             int right = n -1;

//             while (left <= right ) {
//                 int mid = (right - left)/2 + left;
//                 if (nums[mid] == num){
//                     return mid;
//                 } else if (nums[mid] > num){
//                         right = mid -1;
//                     } else{
//                         left = mid + 1;
//                     }
//             }
//             return -1;
//         }

//     }

// }