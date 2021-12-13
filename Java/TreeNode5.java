package com.company;

//108.Convert Sorted Array to Binary Search Tree
//Given a list of ascending int, convert it to a height-balanced binary search tree.
//1 <= nums.length <= 10^4
public class TreeNode5 {
    Node root;
    TreeNode5(){root = null;}
    class Node{
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

    public Node sortedArrayToBST(int arr[], int startIndex, int endIndex) {
        if (startIndex > endIndex)
            return null;
        int mid = (startIndex + endIndex) / 2;
        Node node = new Node(arr[mid]);
        node.left = sortedArrayToBST(arr, startIndex, mid-1);
        node.right = sortedArrayToBST(arr, mid+1, endIndex);
        return node;
    }

// print level by level from root to bottom
    public int height(Node root) {
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
    public void printCurLevel(Node root, int level) {
        if (root == null)
            return;
        if (level == 1)
            System.out.print(root.val + " ");
        else if (level > 1) {
            printCurLevel(root.left, level-1); // if level==3, printCurlevel(root.left.left, 1), then (root.left.right, 1)
            printCurLevel(root.right, level-1); // if level==3, printCurlevel(root.right.left, 1), then (root.right.right, 1)
        }
    }
    public void printLevelOrder(Node root) {
        int h = height(root);
        for (int i=1; i<=h; i++)
            printCurLevel(root, i);
    }

    public static void main(String[] args) {
        TreeNode5 tree = new TreeNode5();

        int nums[] = new int[]{-10,-3,0,5,9};
        int n = nums.length;
        Node root = tree.sortedArrayToBST(nums, 0, n-1);
        tree.printLevelOrder(root);
    }
}
