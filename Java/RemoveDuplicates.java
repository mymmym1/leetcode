package com.company;

import java.util.*;
//nums has already been sorted.
public class RemoveDuplicates {
    public static int removeDuplicates(int[] nums) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (int i=0; i<nums.length; i++)
            if(!list.contains(nums[i]))
                list.add(nums[i]);
        return list.size();
    }
    public static void main(String[] args) {
        int[] nums1 = {0,0,1,1,1,2,2,3,3,4};
        int[] nums2 = {1,1,2};
        int k1 = removeDuplicates(nums1);
        int k2 = removeDuplicates(nums2);
        System.out.println(k2);
    }
}
