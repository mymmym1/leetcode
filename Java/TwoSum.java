package com.company;

import java.util.*;

class TwoSum{
    public static int[] twoSum(int[] nums, int target) {
        int[] indices = new int[2];
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            int curr = nums[left] + nums[right];
            if (curr == target) {
                indices[0] = left;
                indices[1] = right;            
            }                
            if (curr > target) {
                right--;
            } else {
                left++;
            }
        }        
        return indices;
    }
    public static void main(String[] args){
        Scanner in1 = new Scanner(System.in);
        System.out.println("Please input length of nums: ");
        int l = in1.nextInt();
        int[] nums = new int[l];
        System.out.println("Please input nums: ");
        for (int i=0; i<l; i++){
            nums[i] = in1.nextInt();
        }

        System.out.println("Please input target: ");
        int target = in1.nextInt();
        int[] indices = twoSum(nums, target);
        System.out.println(indices[0] +","+indices[1]);
    }
}

