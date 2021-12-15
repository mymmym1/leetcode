package com.company;
import java.util.*;

public class PascalsTriangle {
    static int factorial(int n) {  // n: row index
        int f;
        for (f=1; n>1; n--) {
            f *=n; //e.g. n=4. f=1*4=4, f=4*3=12, f=12*2=24
        }            //or n=2. f=1*2=2
        return f;
    }

    static int binomialCoeff(int n, int r) { // n: row index, r: index in the row
        return factorial(n) / (factorial(n-r) * factorial(r)); //e.g. n=4, r=2; 24/(2*2)=6
    }

    public static List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        for(int i=0; i<numRows; i++) {
            List<Integer> line = new ArrayList<Integer>();
            for(int j=0; j<=i; j++) {
                line.add(binomialCoeff(i, j));
            }
            result.add(line);
        }
        return result;
    }

    public static void main(String args[]) {
        int n = 5;
        System.out.println(generate(n));
    }
}
