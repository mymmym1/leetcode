package com.company;

import java.util.*;

public class RemoveElement {
    public static int removeElement(int[] nums, int val) {
        ArrayList<Integer> list = new ArrayList<Integer> ();
        for (int i=0; i<nums.length; i++) {
            list.add(nums[i]);
        }
        list.removeIf(n->n.equals(val));
        
        return list.size();
    }
    public static void main(String[] args) {
        int[] nums = {0,1,2,3,0,4,2};
        int val = 2;
        System.out.println(removeElement(nums, val));

    }
}
