
public class MoveZeroes{
    public static void (int[] nums){
        int pointer = 0;

        for (int i = 0; i< nums.length; i++){
            if (num != 0){
                int temp = nums[i];
                nums[i] = nums[pointer];
                nums[pointer] = temp;
                pointer++;
            }
        }
    }
    
}