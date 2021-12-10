package com.company;

//Remove duplicates from sorted list

class ListNode2 {
    Node head = null;
    public static class Node{
        int val;
        Node next;
        Node(int val, Node next) {this.val = val; this.next = next;}
    }

    public static void printList(ListNode2 list) {
        Node newHead = list.head;
        while (newHead != null) {
            System.out.print(newHead.val + ",");
            newHead = newHead.next;
        }
    }

    public static ListNode2 insert(ListNode2 list, int value) {
        Node temp = new Node (value, null); //new value to be inserted as a node
        if (list.head == null) {
            list.head = temp;
        }
        else {
            Node end = list.head;
            while (end.next != null){
                end = end.next;  //move forward until find the end node
            }
            end.next = temp;
        }
        return list;
    }

    public static ListNode2 convert(int[] l) {
        ListNode2 newListNode = new ListNode2();
        for (int i=0; i<l.length; i++) {
            newListNode = insert(newListNode, l[i]);
        }
        return newListNode;
    }

    public static ListNode2 deleteDuplicates(ListNode2 list) {
        Node n = list.head;
        Node nextNode = n.next;

        ListNode2 newListnode = new ListNode2();  // can't point to the head of list, otherwise they'll be in the same storage location.
        newListnode.head = new Node(n.val, null);
        while (nextNode != null) {
            if (nextNode.val != n.val) {
                newListnode = insert(newListnode, nextNode.val);
            }
            nextNode = nextNode.next;
            n = n.next;
        }
        return newListnode;
    }

    public static void main(String[] args) {
        int[] l = {1,1,2,3,3};
        ListNode2 list = convert(l);
        printList(deleteDuplicates(list));
    }
}
