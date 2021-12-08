package com.company;

import java.util.*;
//MergeTwoSortedLists, given 2 sorted linked lists: list1 and list2.
//The number of nodes in both lists is in the range [0, 50].
//-100 <= Node.val <= 100

    /** Definition for singly-linked list.*/
class ListNode {
    Node head = null;
    static class Node {
        int val;
        Node next;
        //Node() {}
        //Node(int val) { this.val = val; }
        Node(int val, Node next) { this.val = val; this.next = next; }
    }

    public static ListNode insert(ListNode list, int value) { //insert value to the end of the list
        Node temp = new Node(value, null); //define a new node with the inserted value
        if (list.head == null) { //if the list is empty
            list.head = temp;  //make list head the node to be inserted - temp
        } else {  //if list is not empty, e.g. 1,2,3, find the list's last node:
            Node last = list.head;  //initialize last node as head e.g. 1
            while (last.next != null) {
                last = last.next;
            }
            last.next = temp;  //insert the node to the list's end
        }
        return list;
    }

    public static void printList(ListNode list) {
        Node curNode = list.head;  // first node of the list
        while (curNode != null) {
            System.out.print(curNode.val + ",");
            curNode = curNode.next;
        }
    }

    public static ListNode convert(int[] l) {
        ListNode list = new ListNode(); //create an empty new ListNode
        for (int i=0; i<l.length; i++) {  //insert int list into ListNode one by one
            list = insert(list, l[i]);
        }
        //printList(list);
        return list;
    }

    public static ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ArrayList<Integer> l1 = new ArrayList<Integer>();
        ArrayList<Integer> l2 = new ArrayList<Integer>();
        Node a = list1.head;
        while (a != null) {
            int aa = a.val;
            l1.add(aa);
            a = a.next;
        }
        Node b = list2.head;
        while (b != null) {
            int bb = b.val;
            l2.add(bb);
            b = b.next;
        }
        l1.addAll(l2);
        Collections.sort(l1);
        int[] newList = new int[l1.size()];
        for (int i=0; i<newList.length; i++){
            newList[i] = l1.get(i);
        }
        ListNode linking = convert(newList);

        return linking;
    }

    public static void main(String[] args) {
        int[] l1 = {1,2,4};
        ListNode list1 =  convert(l1);
        //System.out.println();
        int[] l2 = {1,3,4};
        ListNode list2 = convert(l2);
        printList(mergeTwoLists(list1, list2));
    }
}
