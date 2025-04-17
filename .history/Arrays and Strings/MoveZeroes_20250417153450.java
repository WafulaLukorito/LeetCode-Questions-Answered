
public class MoveZeroes{
    public static void moveZeroes (int[] nums){
        int pointer = 0;

        for (i=0; i < nums.length; i++){
            if (nums[i] != 0){
                int temp = nums[i];
                nums[i] = nums[pointer];
                nums[pointer] = temp;
                pointer++;
            }
        }
        public static 
}
}