


// Given a string s, find the length of the longest substring without repeating characters.

import java.util.HashSet;

public class LongestSubstringWithoutRepeatingCharacte {

    public static int lengthOfLongestSubstring (String myString){
        HashSet<Character> mySet = new HashSet<>();
        int left = 0, maxLength = 0;

        for (int right = 0; right < myString.length(); right++) {
            
            char currentChar = myString.charAt(right);

            while (mySet.contains(currentChar)){
                mySet.remove(myString.charAt(left));
                left++;

            }
            mySet.add(currentChar);

            maxLength = Math.max (maxLength, right - left + 1);
        }
        return maxLength;

    }

        public static void main(String[] args) {
        String test1 = "abcabcbb";
        String test2 = "bbbbb";
        String test3 = "pwwkew";
        
        System.out.println("Test 1: " + lengthOfLongestSubstring(test1)); // Expected: 3 ("abc")
        System.out.println("Test 2: " + lengthOfLongestSubstring(test2)); // Expected: 1 ("b")
        System.out.println("Test 3: " + lengthOfLongestSubstring(test3)); // Expected: 3 ("wke")
    }
}