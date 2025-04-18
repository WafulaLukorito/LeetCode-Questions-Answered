

// # *Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

// # ?Time Complexity = O(N) ---- Single loop over container
// # ? Space Complexity = O(1) ---- No external data structures are used

import java.util.Arrays;

public class ContainerWithMostWater {

    public static int[] maxArea(int[] heights) {
        if (heights == null || heights.length < 2) {
            return new int[]{0, 0}; // Edge case: Not enough lines to form a container
        }

        int maxArea = 0;
        int left = 0;
        int right = heights.length - 1;
        int[] bestHeights = new int[2];

        while (left < right) {
            int currentHeight = Math.min(heights[left], heights[right]);
            int width = right - left;
            int currentArea = currentHeight * width;

            if (currentArea > maxArea) {
                maxArea = currentArea;
                bestHeights[0] = heights[left];
                bestHeights[1] = heights[right];
            }

            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }

        return bestHeights;
    }

    public static void main(String[] args) {
        int[] height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        int[] result = maxArea(height);
        System.out.println("Heights for maximum water container area: " + Arrays.toString(result));
    }
}