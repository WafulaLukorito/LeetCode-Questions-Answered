import java.util.Arrays;

public class new_dsa {
    public static int binarySearch(int[] arr, int n) {
        int left = 0, right = arr.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (arr[mid] == n) {
                return mid;
            } else if (arr[mid] > n) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        int[] myArr = { 1, 2, 3, 4 };
        int myNum = 2;
        System.out.println("In the array " + Arrays.toString(myArr) + ", the number " + myNum + " is found at index "
                + binarySearch(myArr, myNum));
    }
}