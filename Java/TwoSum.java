package com.company;

import java.util.*;

class TwoSum{
    public static int[] twoSum(int[] nums, int target) {
        int[] indices = new int[2];
        for (int i=0; i<nums.length; i++) {
            for (int j=0; j<nums.length; j++){
                if ((i!=j) && (nums[i] + nums[j] == target)){
                    indices[1] = i;
                    indices[0] = j;
                }
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

