package com.company;
import java.util.*;

//112. Path Sum
//Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
//adding up all the values along the path equals targetSum. A leaf is a node with no children.
public class TreeNode8 {
    Node root;
    TreeNode8(){root = null;}
    static class Node {
        int val;
        Node left;
        Node right;
        Node(){}
        Node(int val){this.val = val;}
        Node(int val, Node left, Node right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    static int sum = 0;
    static ArrayList<Integer> sums = new ArrayList<Integer>();

    public static ArrayList<Integer> pathSum(Node root) {
        if (root == null) {
            //System.out.print(sums.size());
            //System.out.print(sum + ",");
            return sums;
        }
        else {
            if (root.left == null && root.right == null) {
                sum = sum + root.val;
                pathSum(root.left);
            } else if (root.left != null && root.right == null) {
                sum = sum + root.val;
                pathSum(root.left);
            } else if (root.left == null && root.right != null) {
                sum = sum + root.val;
                pathSum(root.right);
            } else {
                sum = sum + root.val;
                int temp = sum;
                pathSum(root.left);
                sum = temp;
                pathSum(root.right);
            }
        }
        sums.add(sum);
        return sums;
    }

    public static boolean hasPathSum(Node root, int targetSum) {
        ArrayList<Integer> sums = pathSum(root);
        if (sums.contains(targetSum))
            return true;
        else return false;
    }

    public static void main(String[] args) {
        Node root = new Node(5);
        root.left = new Node(4);
        root.right = new Node(8);
        root.left.left = new Node(11);
        root.right.left = new Node(13);
        root.right.right = new Node(4);
        root.left.left.left = new Node(7);
        root.left.left.right = new Node(2);
        root.right.right.right = new Node(1);
        int targetSum = 22;

        /**Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        int targetSum = 5;
         */

        /**Node root = null;
        int targetSum = 0;
         */

        System.out.println(hasPathSum(root, targetSum));
    }
}
