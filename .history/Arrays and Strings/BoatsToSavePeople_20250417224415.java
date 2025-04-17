// # * You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

// # *Return the minimum number of boats to carry every given person.

import java.util.Arrays;

public class BoatsToSavePeople {

    public static int numBoats(int[] people, int limit){
        int left = 0;
        int right = people.length - 1;
        int boats = 0;

        Arrays.sort(people);

        while (left <= right){
            if ((left + right) <= limit){
                boats++;
                left++;
                right--;
            }
            else {
                boats++;
                right --;
            }
        }


        return boats;

    }

    public static void main(String[] args) {
        
        int[] people = {3, 2, 2, 1};
        int limit = 3;
        System.out.println("Minimum boats needed: " + numBoats(people, limit));
    }
    
}


