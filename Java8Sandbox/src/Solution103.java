import java.util.ArrayList;
import java.util.List;

/**
 * https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
 * @author Rays
 *
 */
public class Solution103 {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
		List<List<Integer>> list = new ArrayList<List<Integer>>();
		levelOrder(root, list, 0);
		return list;
    }

	private void levelOrder(TreeNode node, List<List<Integer>> levelOrderList, int level) {
		if (node != null) {
			List<Integer> list ;
			if (level > levelOrderList.size() - 1) {
				list = new ArrayList<Integer>();
				levelOrderList.add(list);
			} else {
				list = levelOrderList.get(level);
			}
			if (level % 2 == 0) {
				list.add(node.val);
			} else {
				list.add(0, node.val);
			}

			if (node.left != null) {
				levelOrder(node.left, levelOrderList, level + 1);
			}
			if (node.right != null) {
				levelOrder(node.right, levelOrderList, level + 1);
			}
		}
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
    	Solution103 a = new Solution103();
    	System.out.println("List: " + a.zigzagLevelOrder(root1));
    	TreeNode root2 = new TreeNode(6);
    	root2.left = new TreeNode(8);
    	root2.left.left = new TreeNode(9);
    	root2.left.right = new TreeNode(7);
    	root2.right = new TreeNode(5);
    	root2.right.right = new TreeNode(4);
    	System.out.println("List: " + a.zigzagLevelOrder(root2));
    	TreeNode root3 = new TreeNode(1);
    	root3.left = new TreeNode(2);
    	root3.left.left = new TreeNode(3);
    	root3.right = new TreeNode(4);
    	root3.right.right = new TreeNode(5);
    	System.out.println("List: " + a.zigzagLevelOrder(root3));
    	TreeNode root4 = null;
    	System.out.println("List: " + a.zigzagLevelOrder(root4));
    }
}
