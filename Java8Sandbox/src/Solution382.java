
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution382 {
	ListNode head;
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    public Solution382(ListNode head) {
        this.head = head;
    }

    /** Returns a random node's value. */
    public int getRandom() {
    	ListNode node = head;
    	int n = 1;
    	while (node.next != null) {
    		n++;
    		node = node.next;
    	}
    	int index = (int)(Math.random()*n);
    	node = head;
    	for (int i=0; i<index; i++) {
    		node = node.next;
    	}
    	return node.val;
    }
}

