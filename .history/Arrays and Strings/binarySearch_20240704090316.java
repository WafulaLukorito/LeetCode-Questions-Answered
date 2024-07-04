
public class BinarySearch{

    public static void main(String[] args) {
        int[] nums = {1,2,3,4,5,6,7};
        int num = 5;
        System.out.println(binarySearch(nums, num));
    }

    public static int binarySearch(int[] nums, int num){
        int n = nums.length;
        if (n < 1){
            return -1;
        } else {
            int left = 0;
            int right = n -1;

            while (left <= right ) {
                int mid = (right - left)/2 + left;
                if (nums[mid] == num){
                    return mid;
                } else {
                    if (nums[mid] > num){
                        right = mid -1;
                    } else{
                        left = mid + 1;
                    }
                }
                return -1;
            }
          
        }

    }

}