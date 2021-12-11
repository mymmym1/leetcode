package com.company;

import java.util.*;
public class MergeSortedArray {
    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        ArrayList<Integer> n1 = new ArrayList<Integer>();
        ArrayList<Integer> n2 = new ArrayList<Integer>();
        for (int i=0; i<m; i++)
            n1.add(nums1[i]);
        for (int i=0; i<n; i++)
            n2.add(nums2[i]);
        n1.addAll(n2);
        Collections.sort(n1);
        for (int i=0; i<m+n; i++) {
            nums1[i] = n1.get(i);
            System.out.print(nums1[i] + ",");
        }
    }
    public static void main(String[] args) {
        int[] nums1 = {1,2,3,0,0,0};
        int[] nums2 = {2,5,6};
        int m = 3;
        int n = 3;
        merge(nums1, m, nums2, n);
    }
}
