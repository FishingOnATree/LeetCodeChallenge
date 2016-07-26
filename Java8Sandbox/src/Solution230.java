import java.util.ArrayList;
import java.util.List;

/**
 * https://leetcode.com/problems/kth-smallest-element-in-a-bst/
 * @author Rays
 *
 */
public class Solution230 {
    public int kthSmallest(TreeNode root, int k) {
    	List<TreeNode> list = inorderTravesal(root);
    	// System.out.print("[");
    	// for(TreeNode node: list) {
    	//	  System.out.print(node.toString() + " ");
    	// }
    	// System.out.print("] \n");
    	if (list.get(0).val < list.get(list.size()-1).val) {
    		return list.get(k-1).val;
    	} else {
    		return list.get(list.size()-k).val;
    	}

    }

    private List<TreeNode> inorderTravesal(TreeNode node) {
    	List<TreeNode> list = new ArrayList<TreeNode>();
    	if (node.left != null) {
    		list.addAll(inorderTravesal(node.left));
    	}
    	list.add(node);
    	if (node.right != null) {
    		list.addAll(inorderTravesal(node.right));
    	}
    	return list;
    }

    public static void main(String[] args) {
    	TreeNode root1 = new TreeNode(6);
    	root1.left = new TreeNode(3);
    	root1.left.left = new TreeNode(2);
    	root1.left.left.left = new TreeNode(1);
    	root1.left.right = new TreeNode(4);
    	root1.left.right.right = new TreeNode(5);
    	root1.right = new TreeNode(9);
    	root1.right.left = new TreeNode(7);
    	root1.right.left.right = new TreeNode(8);
    	root1.right.right = new TreeNode(11);
    	root1.right.right.left = new TreeNode(10);
    	root1.right.right.right = new TreeNode(12);
    	Solution230 a = new Solution230();
    	System.out.println("3rd smallest: " + a.kthSmallest(root1, 3));
    	TreeNode root2 = new TreeNode(6);
    	root2.left = new TreeNode(8);
    	root2.left.left = new TreeNode(9);
    	root2.left.right = new TreeNode(7);
    	root2.right = new TreeNode(5);
    	root2.right.right = new TreeNode(4);
    	System.out.println("3rd smallest: " + a.kthSmallest(root2, 3));
    }
}


class TreeNode {
	int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
    @Override
    public String toString() { return Integer.toString(val); }
}