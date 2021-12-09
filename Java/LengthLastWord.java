package com.company;

public class LengthLastWord {
    public static int lengthOfLastWord(String s) {
        String[] words = s.split(" ");
        int last = words.length - 1;
        return words[last].length();
    }
    public static void main(String[] args) {
        String s1 = "Hello World";
        String s2 = "   fly me   to   the moon  ";
        String s3 = "luffy is still joyboy";
        System.out.println(lengthOfLastWord(s3));
    }
}
