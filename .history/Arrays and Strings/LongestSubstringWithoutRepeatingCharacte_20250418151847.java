


// Given a string s, find the length of the longest substring without repeating characters.

import java.util.HashSet;

public class LongestSubstringWithoutRepeatingCharacte {

    public static int longestSubstring (String myString){
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
}