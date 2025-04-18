

// # *Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

// # ?Time Complexity = O(N) ---- Single loop over container
// # ? Space Complexity = O(1) ---- No external data structures are used

import java.util.Arrays;

public class ContainerWithMostWater{

    public static int[] maxArea (int[] heights){
       int maxArea = 0, currentArea= 0, left = 0, right = height.length -1;
       int[] bestHeights = new int[2];

       while (left < right){
        int width = right - left;
        currentArea = Math.min(heights[right], heights[left]) * width;

        if (currentArea > maxArea){
            bestHeights[0] = heights[left];
            bestHeights[1] = heights[right];
            maxArea = currentArea;
        }

        if (heights[left] < heights[right]){
            left++;
        } else {
            right --;
        }

       }
        }


        return bestLines;
    }
     public static void main(String[] args) {
        int[] height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        System.out.println("Heights for Maximum water container area: " + Arrays.toString(maxArea(height)));
    }
}