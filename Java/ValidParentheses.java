package com.company;
// 1 <= s.length <= 10^4
// s consists of parentheses only '()[]{}'.
// This method can be simplified in another way.
public class ValidParentheses {
    public static String mksbstring(String s, int a, int b){
        String subs = s.substring(a, b);
        return subs;
    }

    public static boolean isValid(String s) {
        boolean result = false;
        String ms = s;

        while (ms.length() > 0) {
            outerloop:
            for (int i = 0; i < ms.length(); i++) {
                if (ms.charAt(i) == '(') {
                    for (int j = ms.length() - 1; j > i; j--) {
                        if (ms.charAt(j) == ')') {
                            if (j - i == 1) {
                                result = true;
                                if (ms.length()==2) return true;
                            }
                            else {
                                ms = mksbstring(s, i + 1, j);
                                break outerloop;
                            }
                        }
                    }
                }
                if (ms.charAt(i) == '[') {
                    for (int j = ms.length() - 1; j > i; j--) {
                        if (ms.charAt(j) == ']') {
                            if (j - i == 1) {
                                result = true;
                                if (ms.length()==2) return true;
                            }
                            else {
                                ms = mksbstring(s, i + 1, j);
                                break outerloop;
                            }
                        }
                    }
                }
                if (ms.charAt(i) == '{') {
                    for (int j = ms.length() - 1; j > i; j--) {
                        if (ms.charAt(j) == '}') {
                            if (j - i == 1) {
                                result = true;
                                if (ms.length()==2) return true;
                            }
                            else {
                                ms = mksbstring(s, i + 1, j);
                                break outerloop;
                            }
                        }
                    }
                }
                return false;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        String s = "()[]{(";
        System.out.println(isValid(s));
    }
}
