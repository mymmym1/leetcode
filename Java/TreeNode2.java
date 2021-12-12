package com.company;

// Check if two binary trees are the same.
public class TreeNode2 {
    Node root;
    TreeNode2(){
        root = null;
    }

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

    static void printInorder(Node n) {
        if (n != null) {
            printInorder(n.left);
            System.out.print(n.val + ",");
            printInorder(n.right);
        }
    }

    public static boolean isSameTree(Node p, Node q) {
        if (p == null && q == null)
            return true;

        if (p != null && q != null) {
            return (p.val == q.val
                    && isSameTree(p.left, q.left)
                    && isSameTree(p.right, q.right));
        }
        return false;
    }

    public static void main(String[] args) {
        TreeNode2 treeP = new TreeNode2();
        TreeNode2 treeQ = new TreeNode2();

        treeP.root = new Node(1);
        treeP.root.left = new Node(2);
        treeP.root.right = new Node(3);

        treeQ.root = new Node(1);
        treeQ.root.left = new Node(2);
        treeQ.root.right = new Node(3);

        System.out.println(isSameTree(treeP.root, treeQ.root));

    }

}
