


// Given a string s, find the length of the longest substring without repeating characters.

import java.util.HashSet;
import java.util.Set;

public class LongestSubstringWithoutRepeatingCharacte {

    public static int lengthOfLongestSubstring (String s){
       HashSet<Character> charSet = new HashSet<>();

       int left = 0;

       for (r)

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