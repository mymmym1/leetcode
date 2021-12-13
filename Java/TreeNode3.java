package com.company;

//Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
//The number of nodes in the tree is in the range [1, 1000].
public class TreeNode3 {
    Node root;
    TreeNode3(){
        root = null;
    }
    static class Node{
        int val;
        Node left;
        Node right;
        Node(){};
        Node(int val) {this.val = val;}
        Node(int val, Node left, Node right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public static boolean isSymmetric(Node p, Node q) {
        if (p == null && q == null) return true;
        if (p != null && q != null) {
            return (p.val == q.val
                    && isSymmetric(p.left, q.right)
                    && isSymmetric(p.right, q.left));
        }
        return false;
    }

    public static void main(String[] args) {
        Node pp = null; //new Node(3);
        Node pq = new Node(3);
        Node qp = null;//new Node(4);
        Node qq = new Node(3);
        Node p = new Node(2, pp, pq);
        Node q = new Node(2, qp, qq);
        System.out.println(isSymmetric(p, q));
    }
}