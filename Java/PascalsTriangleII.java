package com.company;
import java.util.*;

//Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
public class PascalsTriangleII {
    static int factorial(int n) {
        int f;
        for (f=1; n>1; n--) {
            f *= n;
        }
        return f;
    }
    static int binomialCoeff(int n, int r) {
        return factorial(n)/(factorial(n-r) * factorial(r));
    }
    static List<Integer> getRow(int numRows, int rowIndex) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        for (int i=0; i<numRows; i++) {
            ArrayList<Integer> line = new ArrayList<Integer>();
            for (int j=0; j<=i; j++) {
                line.add(binomialCoeff(i,j));
            }
            result.add(line);
        }
        return result.get(rowIndex);
    }
    public static void main(String[] args) {
        System.out.println(getRow(5,3));
    }
}
