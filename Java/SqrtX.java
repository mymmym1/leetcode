package com.company;
//x is non-negative, built-in exponent function or operator is not allowed.
//Truncate result to integer
public class SqrtX {
    public static int mySqrt(int x) {
        int result = -1;
        for (int i=0; i<=x/2; i++){
            int compare = i*i;
            if (compare == x)
                result = i;
            else if (compare > x) {
                result = i-1;
                break;
            }
        }
        return result;

    }
    public static void main(String[] args) {
        int x = 8;
        System.out.println(mySqrt(x));
    }
}
