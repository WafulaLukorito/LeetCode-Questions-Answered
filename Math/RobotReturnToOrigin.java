/*
""" 
There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

 
Example 1:

Input: moves = "UD"
Output: true
Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.

#? TimeComplexity O(N).. Loop over string

#? Space complexity O(1)...don't create additional memory
"""
 */

 public class RobotReturnToOrigin{
    public static boolean robotReturnToOrigin(String moves){
        int x = 0, y = 0;

        for (char c : moves.toCharArray()){
            if (c == 'U') y++;
            if (c=='D') y--;
            if (c == 'L') x--;
            if (c=='R') x++;
        }
        return (x==0 && y==0);

    }
 }

 /*public static boolean judgeCircle(String moves) {
    int x = 0, y = 0;
    for (char c : moves.toCharArray()) {
        switch (c) {
            case 'U': y++; break;
            case 'D': y--; break;
            case 'L': x--; break;
            case 'R': x++; break;
        }
    }
    return (x == 0 && y == 0);
} */