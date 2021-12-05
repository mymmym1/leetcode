package com.company;
import java.util.*;

class RomanToInteger {
    public static int romanToInt(String s) {
        ArrayList<String> sl = new ArrayList<String>();
        for (int i=0; i<s.length(); i++) {
            String s1 = Character.toString(s.charAt(i));
            if ((i + 1) < s.length()) {
                String s2 = Character.toString(s.charAt(i + 1));
                if (s1.equals("I") && s2.equals("V")) {
                    s1 = "IV";
                    i++;
                } else if (s1.equals("I") && s2.equals("X")) {
                    s1 = "IX";
                    i++;
                } else if (s1.equals("X") && s2.equals("L")) {
                    s1 = "XL";
                    i++;
                } else if (s1.equals("X") && s2.equals("C")) {
                    s1 = "XC";
                    i++;
                } else if (s1.equals("C") && s2.equals("D")) {
                    s1 = "CD";
                    i++;
                } else if (s1.equals("C") && s2.equals("M")) {
                    s1 = "CM";
                    i++;
                }
            }
            sl.add(s1);
        }
        int n = 0;
        int result = 0;
        for (int i=0; i<sl.size(); i++) {
            String s1 = sl.get(i);
            switch (s1) {
                case "IV": n = 4; break;
                case "IX": n = 9; break;
                case "XL": n = 40; break;
                case "XC": n = 90; break;
                case "CD": n = 400; break;
                case "CM": n = 900; break;
                case "I":
                    n = 1;
                    break;
                case "V":
                    n = 5;
                    break;
                case "X":
                    n = 10;
                    break;
                case "L":
                    n = 50;
                    break;
                case "C":
                    n = 100;
                    break;
                case "D":
                    n = 500;
                    break;
                case "M":
                    n = 1000;
                    break;
                default:
                    System.out.println("Contains illegal symbol!");
                    break;
            }
            result += n;
        }
    return result;
    }

    public static void main(String[] args) {
        String s = "MCMXCIV";
        System.out.println(romanToInt(s));
    }
}
