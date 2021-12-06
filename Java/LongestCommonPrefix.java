package com.company;

class LongestCommonPrefix {
    public static String longestCommonPrefix(String[] strs) {
        String s = "";
        for (int i=0; i<strs.length; i++){
            for (int j=0; j<strs[i].length(); j++){
                char c1 = strs[i].charAt(j);
                for (int k=1; k<strs.length-i; k++){
                    char c2;
                    if (strs[i+k].length() > j) {
                        c2 = strs[i + k].charAt(j);
                        if (c1 != c2)
                            return s;
                        else {
                            if (k+i == strs.length-1)
                                s += c2;
                            else continue;
                        }
                    }
                    else return s;
                }
            }
            if (s == "") continue;
            else break;
        }
        return s;
    }
    public static void main(String[] args) {
        String[] strs = {"rac","racecar","rack"};
        //String[] strs = {"flower","flow","flight"};
        //String[] strs = {"dog","racecar","car"};
        System.out.println(longestCommonPrefix(strs));
    }
}
