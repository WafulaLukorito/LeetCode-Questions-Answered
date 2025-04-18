

// # *Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

// # ?Time Complexity = O(N) ---- Single loop over container
// # ? Space Complexity = O(1) ---- No external data structures are used

public class ContainerWithMostWater{

    public static int[] maxArea (int[] height){
        int maxArea = 0;
        int currentArea = 0;
        int left = 0;
        int right = height.length - 1;
        int [] bestCoordinates = new int[2];

        while (left < right){
            int width = right - left;
            currentArea = Math.max(Math.min(height[right], height[left]) * width, maxArea);

            //update bestCoordinates
            if (currentArea > maxArea){
                bestCoordinates[0] = left;
                bestCoordinates[1] = right;
                maxArea = currentArea;
            }


            //move pointer with smaller height
            if (height[right] > height[left]){
                left ++;
            } else {
                right --;
            }
        }


        return bestCoordinates;
    }
     public static void main(String[] args) {
        int[] height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        System.out.println("Coordinates for Maximum water container area: " + maxArea(height));
    }


}