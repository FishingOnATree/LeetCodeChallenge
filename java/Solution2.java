/*
 * https://leetcode.com/problems/add-two-numbers/
 * 
 * You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order 
 * and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 */


public class Solution2 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode n1 = l1, n2 = l2;
        ListNode node = null, prevNode = null;
        int quotient = 0;
        while (n1 != null || n2 != null) {
        	int value1 = n1==null? 0:n1.val;
        	int value2 = n2==null? 0:n2.val;
        	int sum = value1 + value2 + quotient;
        	ListNode tmp = new ListNode(sum%10);
        	quotient = sum / 10;
        	if (prevNode == null) {
        		node = tmp;
        	} else {
        		prevNode.next = tmp;
        	}
        	prevNode = tmp;
        	if (n1 != null) {
        		n1 = n1.next;
        	}
        	if (n2 != null) {
        		n2 = n2.next;
        	}
        }
        if (quotient > 0) {
        	prevNode.next = new ListNode(quotient);
        }
    	return node;
    }
    
    
    private ListNode convertToListNode(int num) {
    	ListNode root = null, ln = null, prevNode = null;
    	int n = num;
    	while (n > 0) {
    		prevNode = ln;
    		ln = new ListNode(n%10);
    		n = n / 10;    		
    		if (prevNode == null) {
    			root = ln;
    		} else {
    			prevNode.next = ln;
    		}
    		prevNode = ln;
    	}
    	return root;
    }
    
    public static void main(String args[]) {
    	Solution2 a = new Solution2();
    	System.out.println(a.convertToListNode(103));
    	System.out.println(a.convertToListNode(5));
    	System.out.println(a.convertToListNode(30109));
    	System.out.println(a.convertToListNode(9100003));
    	System.out.println("==================");
    	ListNode a1, a2, a3, a4;
    	a1 = a.convertToListNode(106);
    	a2 = a.convertToListNode(916);
    	System.out.println(a.addTwoNumbers(a1, a2));
    	a3 = a.convertToListNode(75001);
    	a4 = a.convertToListNode(309);
    	System.out.println(a.addTwoNumbers(a3, a4));
    	System.out.println("==================");
    }
}


class ListNode {
     int val;
     ListNode next;
     ListNode(int x) { val = x; }
     public String toString(){
    	 ListNode node = this;
    	 StringBuilder sb = new StringBuilder();
    	 while (node != null) {
    		 sb.append(Integer.toString(node.val));
    		 node = node.next;
    	 }
    	 return sb.toString();
     }
}