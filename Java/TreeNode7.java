package com.company;

//111.Minimum Depth of Binary Tree
public class TreeNode7 {
    Node root;
    TreeNode7(){root = null;}
    static class Node {
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

    public static int minDepth(Node n) {
        if (n == null)
            return 0;
        if (n.left == null && n.right == null) //A single node means both root and leaf.
            return 1;
        if (n.left == null)
            return minDepth(n.right) + 1;
        if (n.right == null)
            return minDepth(n.left) + 1;
        return Math.min(minDepth(n.left), minDepth(n.right)) + 1;
    }
    public static void main(String[] args) {
        Node root = new Node(2);
        root.right = new Node(3);
        root.right.right = new Node(4);
        root.right.right.right = new Node(5);
        root.right.right.right.right = new Node(6);

        /**Node root = new Node(3);
        root.left = new Node(9);
        root.right = new Node(20);
        root.right.left = new Node(15);
        root.right.right = new Node(7);*/

        System.out.println(minDepth(root));
    }
}
