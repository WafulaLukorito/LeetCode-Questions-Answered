// """
// You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

// Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

// You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
// """

public class firstBadVersion {

    //Sample Defined API
    private static boolean isBadVersion(int version){
        int firstBad = 4;
        return version >= firstBad;
    }

    public static int findFirstBadVersion(int n){
       int left = 1, right = n;

       while (left < right){
        int mid = left + (right - left)/2;

        if (isBadVersion(mid)){
            right = mid;

        } else {
            left = mid+1;
        }
       }
       return left;
    }
       public static void main(String[] args) {
        int n = 5;
        System.out.println("First bad version: " + findFirstBadVersion(n)); // Expected: 4
    }

}