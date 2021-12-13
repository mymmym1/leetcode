package com.company;

//110. Balanced Binary Tree
//Left and right subtrees of every node differ in height by no more than 1.
public class TreeNode6 {
    Node root;
    TreeNode6(){root = null;}
    static class Node{
        int val;
        Node left;
        Node right;
        Node(){}
        Node(int val) {this.val = val;}
        Node(int val, Node left, Node right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
    public static int height(Node root) {
        if (root == null)
            return 0;
        else {
            int lheight = height(root.left);
            int rheight = height(root.right);
            if (lheight > rheight)
                return lheight + 1;
            else
                return rheight + 1;
        }
    }
    public static boolean isBalanced(Node root) {
        if (root != null) {
            int leftHeight = height(root.left);
            int rightHeight = height(root.right);
            int diff = Math.abs(leftHeight - rightHeight);
            if (diff == 0 || diff == 1) return true;
            else return false;
        }
        else return true;
    }
    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(2);
        root.left.left = new Node(3);
        root.left.right = new Node(3);
        root.left.left.left = new Node(4);
        root.left.left.right = new Node(4);
        System.out.println(isBalanced(root));

    }
}
