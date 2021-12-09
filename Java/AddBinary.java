package com.company;

public class AddBinary {
    public static String addBinary(String a, String b) {
        int first = Integer.parseInt(a, 2);
        int second = Integer.parseInt(b, 2);
        int sum = first + second;
        String result = Integer.toBinaryString(sum);
        return result;
    }
    public static void main(String[] args) {
        String a = "1010";
        String b = "1011";
        System.out.println(addBinary(a, b));
    }
}
