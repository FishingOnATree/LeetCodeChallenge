
public class ListNode {
     int val;
     ListNode next;
     ListNode(int x) { val = x; }
     @Override
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