/**
 * https://leetcode.com/problems/minimum-depth-of-binary-tree/
 * @author Rays
 *
 */
public class Solution111 {
    public int minDepth(TreeNode node) {
		int ans = 0;
		if (node != null) {
			if (node.left != null) {
				ans = minDepth(node.left);
			}
			if (node.right != null) {
				if (node.left == null) {
					ans = minDepth(node.right);
				} else {
					int rDepth = minDepth(node.right);
					ans = (ans < rDepth ? ans : rDepth);
				}
			}
			ans++;
		}
		return ans;
    }


    public static void main(String[] args) {
    	TreeNode root1 = new TreeNode(6);
    	root1.left = new TreeNode(3);
    	//root1.left.left = new TreeNode(2);
    	//root1.left.left.left = new TreeNode(1);
    	//root1.left.right = new TreeNode(4);
    	//root1.left.right.right = new TreeNode(5);
    	root1.right = new TreeNode(9);
    	root1.right.left = new TreeNode(7);
    	root1.right.left.right = new TreeNode(8);
    	root1.right.right = new TreeNode(11);
    	root1.right.right.left = new TreeNode(10);
    	root1.right.right.right = new TreeNode(12);
    	Solution111 a = new Solution111();
    	System.out.println("List: " + a.minDepth(root1));
    	TreeNode root2 = new TreeNode(6);
    	root2.left = new TreeNode(8);
    	root2.left.left = new TreeNode(9);
    	root2.left.right = new TreeNode(7);
    	root2.right = new TreeNode(5);
    	root2.right.right = new TreeNode(4);
    	System.out.println("List: " + a.minDepth(root2));
    	TreeNode root3 = new TreeNode(2);
    	root3.left = new TreeNode(4);
    	System.out.println("List: " + a.minDepth(root3));

    }

}
