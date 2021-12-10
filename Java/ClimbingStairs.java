package com.company;

public class ClimbingStairs {
    public static int climbStairs(int n) {
        int ways = 1;
        while (n > 1) {
            ways += n - 1;
            n -= 2;
        }
        return ways;
    }
    public static void main(String[] args) {
        int n = 4;
        System.out.print(climbStairs(n));
    }
}
