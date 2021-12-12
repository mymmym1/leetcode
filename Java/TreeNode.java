package com.company;

//Binary Tree Inorder Traversal
public class TreeNode {
    Node root;
    TreeNode() {
        root = null;
    }

    static class Node {
        int val;
        Node left;
        Node right;
        Node() {}
        Node(int val) { this.val = val; }
        Node(int val, Node left, Node right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    static void printInorder(Node n) { //print in order means: left->root->right
        if (n != null) {
            printInorder(n.left);
            System.out.print(n.val + ",");
            printInorder(n.right);
        }
    }

    public static void inorderTraversal(Node root) {
            printInorder(root);
    }

    public static void main(String[] args) {
        TreeNode tree = new TreeNode();
        tree.root = new Node(1);
        tree.root.left = null; //new Node(2);
        tree.root.right = new Node(2);
        //tree.root.right.left = null;//new Node(3);

        inorderTraversal(tree.root);
    }

}
