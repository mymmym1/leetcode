package com.company;

//Find the maximum depth of a binary tree.
public class TreeNode4 {
    Node root;
    TreeNode4(){root = null;}
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
    public int maxDepth(Node n) {
        if (n == null)
            return 0;
        else {
            int lDepth = maxDepth(n.left);
            int rDepth = maxDepth(n.right);

            if (lDepth > rDepth)
                return lDepth + 1;
            else
                return rDepth + 1;
        }
    }
    public static void main(String[] args) {
        TreeNode4 tree = new TreeNode4();
        tree.root = new Node(3);
        tree.root.left = new Node(9);
        tree.root.right = new Node(20);
        tree.root.right.left = new Node(15);
        tree.root.right.right = new Node(7);

        System.out.println(tree.maxDepth(tree.root));
    }
}
