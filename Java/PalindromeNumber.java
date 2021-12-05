package com.company;

class PalindromeNumber {
    public static boolean isPalindrome(int x) {
        String s = Integer.toString(x);
        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i) == (s.charAt(s.length()-1-i)))
                return true;
            else return false;
        }
        return false;
    }

    public static void main(String[] args) {
        int x = -101;
        System.out.println(isPalindrome(x));
    }
}
