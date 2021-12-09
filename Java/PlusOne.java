package com.company;

public class PlusOne {
    public static int[] plusOne(int[] digits) {
        String newNum = "";
        int[] result = {};
        for (int i=0; i<digits.length; i++) {
            newNum += digits[i];
        }
        if (newNum != "") {
            int num = Integer.valueOf(newNum);
            num += 1;
            newNum = Integer.toString(num);
            result = new int[newNum.length()];
            for (int i=0; i<result.length; i++) {
                result[i] = Character.getNumericValue(newNum.charAt(i));
            }
        }
        else
            System.out.println("Invalid input!");
        return result;
    }
    public static void main(String[] args) {
        int[] digits = {9};
        int[] result = plusOne(digits);
        for (int i=0; i<result.length-1; i++)
            System.out.print(result[i] + ",");
        System.out.print(result[result.length-1]);
    }
}
