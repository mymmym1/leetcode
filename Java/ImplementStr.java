package com.company;

public class ImplementStr {
    public static int strStr(String haystack, String needle) {
        boolean result = false;
        if (needle == "") return 0;
        else {
            for (int i=0; i<haystack.length(); i++) {
                if (haystack.charAt(i) != needle.charAt(0))
                    continue;
                else {
                    if (haystack.length() - i >= needle.length()) {
                        for (int j=0; j<needle.length(); j++) {
                            if (needle.charAt(j) == haystack.charAt(i + j))
                                result = true;
                            else return -1;
                        }
                    } else return -1;
                    if (result == true) return i;
                }
            }
        }
        return -1;
    }
    
    public static void main(String[] args) {
        String haystack = "hello";
        String needle = "ll";
        System.out.println(strStr(haystack, needle));
    }
}
