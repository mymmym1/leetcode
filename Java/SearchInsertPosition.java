package com.company;

//check if this is with O(log n) runtime complexity.
public class SearchInsertPosition {
    public static int searchInsert(int[] nums, int target) {
        for (int i=0; i<nums.length; i++){
            if (nums[i] != target) {
                if (nums.length == 1) {
                    if (target < nums[0]) return i;
                    else return i+1;
                }
                if (i < nums.length -1)
                    if (target < nums[i]) return i;
                else return i+1;
            }
            else return i;
        }
        return -1;
    }
    public static void main(String[] args) {
        int[] nums = {1};
        int target = 0;
        System.out.println(searchInsert(nums, target));
    }
}
