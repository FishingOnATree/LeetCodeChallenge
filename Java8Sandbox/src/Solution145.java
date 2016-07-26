import java.util.ArrayList;
import java.util.List;

/**
 * https://leetcode.com/problems/binary-tree-postorder-traversal/
 * @author Rays
 *
 */
public class Solution145 {
    public List<Integer> postorderTraversal(TreeNode node) {
		List<Integer> list = new ArrayList<Integer>();
		if (node != null) {
			if (node.left != null) {
				list.addAll(postorderTraversal(node.left));
			}
			if (node.right != null) {
				list.addAll(postorderTraversal(node.right));
			}
			list.add(node.val);
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
    	Solution145 a = new Solution145();
    	System.out.println("List: " + a.postorderTraversal(root1));
    	TreeNode root2 = new TreeNode(6);
    	root2.left = new TreeNode(8);
    	root2.left.left = new TreeNode(9);
    	root2.left.right = new TreeNode(7);
    	root2.right = new TreeNode(5);
    	root2.right.right = new TreeNode(4);
    	System.out.println("List: " + a.postorderTraversal(root2));
    }
}
