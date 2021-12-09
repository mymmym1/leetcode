package com.company;

public class MaximumSubarray {
    public static int maxSubArray(int[] nums) {
        int sum = nums[0];
        int result = nums[0];
        for (int i=0; i<nums.length; i++) {
            if (nums[i] > sum)
                sum = nums[i];
            if (i < nums.length-1) {
                result = nums[i];
                for (int l = 1; l < nums.length - i; l++) {
                    result += nums[i + l];
                    if (result > sum)
                        sum = result;
                }
            }
        }
        return sum;
    }
    public static void main(String[] args) {
        int[] nums1 = {-2,1,-3,4,-1,2,1,-5,4};
        int[] nums2 = {1};
        int[] nums3 = {5,4,-1,7,8};
        System.out.println(maxSubArray(nums1));
    }
}
