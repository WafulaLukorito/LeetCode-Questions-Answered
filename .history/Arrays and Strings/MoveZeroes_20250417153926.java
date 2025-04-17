
public class MoveZeroes{
    public static void moveZeroes (int[] nums){
        int pointer = 0;

        for (int i=0; i < nums.length; i++){
            if (nums[i] != 0){
                int temp = nums[i];
                nums[i] = nums[pointer];
                nums[pointer] = temp;
                pointer++;
            }
        }
       
}
 public static void main(String[] args){
    int[] nums = {0,1,2,0,5,0,7};
    moveZeroes(nums);
    System.out.println(Arrays.toString(nums));

 }
}