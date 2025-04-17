import java.util.Arrays;

// The array shifting approach moves all zeroes to the end by shifting non-zero elements forward without swapping. Instead of swapping each non-zero element individually, this method shifts the non-zero elements in one pass and then fills the remaining positions with zeroes.
// Approach:
// - Use a pointer (index) to track where the next non-zero element should go.
// - Traverse the array:
// - If a number is non-zero, place it at index and increment index.
// - Fill remaining positions with zeros after all non-zero elements are placed.
// Java Implementation (Array Shifting Approach)


public class MoveZeroes{
    public static void moveZeroes(int[] nums){
        int pointer = 0;

        for (int num : nums){
            if (num != 0){
                nums[pointer++]= num;
            }
        }

        while (pointer < nums.length){
            nums[pointer++] = 0;
        }
    }

     public static void main (String[] args) {
         int[] nums = {0, 1, 2, 0, 5, 0, 7};

        moveZeroes(nums);
        System.out.println(Arrays.toString(nums));
    }
}






/**  public class MoveZeroes{
    public static void moveZeroes(int[] nums){
        int pointer = 0;

        for (int i = 0; i< nums.length; i++){
          if (nums[i] != 0) {
             if (i != pointer) { // Only swap if needed
        int temp = nums[i];
        nums[i] = nums[pointer];
        nums[pointer] = temp;
    }
    pointer++;
}
        }
    }
    public static void main (String[] args) {
         int[] nums = {0, 1, 2, 0, 5, 0, 7};

        moveZeroes(nums);
        System.out.println(Arrays.toString(nums));
    }
}
    **/