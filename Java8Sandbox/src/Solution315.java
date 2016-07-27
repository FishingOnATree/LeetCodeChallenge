import java.util.ArrayList;
import java.util.List;

public class Solution315 {
	public List<Integer> countSmaller(int[] nums) {
		int n = nums.length;
		int[] ans = new int[n];
		List<Integer> returnAns = new ArrayList<Integer>(n);
		List<Integer> sortedList = new ArrayList<Integer>(n);
		for (int index = n-1; index >= 0; index--) {
			int pos = binarySearch(sortedList, nums[index]);
			//System.out.println(nums[index] + ", " +  sortedList + ", " + (pos==-1?sortedList.size():pos));
			if (pos == -1) {
				ans[index] = sortedList.size();
				sortedList.add(nums[index]);
			} else {
				ans[index] = pos;
				sortedList.add(pos, nums[index]);
			}
		}
		for (int i = 0; i <ans.length; i++) {
			returnAns.add(ans[i]);
		}
		return returnAns;
    }

	private int binarySearch(List<Integer> list, int target) {
		int lb = 0, ub = list.size() - 1;
		int pos = -1;
		if (list.size() > 0) {
			while (lb < ub) {
				int mid = (lb + ub) / 2;
				if (list.get(mid) == target) {
					pos = mid;
					break;
				} else if (list.get(mid) > target) {
					ub = mid;
				} else {
					if (lb == mid) break;
					lb = mid;
				}
			}
			if (pos < 0) {
				if (target > list.get(ub)) {
					pos = -1; // insert at the end
				} else if (target > list.get(lb)) {
					pos = lb + 1;
				} else {
					pos = lb;
				}
			}
			while (pos > 0 && list.get(pos).equals(list.get(pos - 1))) {
				if (list.get(pos) == 197) {
					System.out.println(pos);
				}
				pos--;
			}
		}
		return pos;
	}

	public List<Integer> countSmaller2(int[] nums) {
		int n = nums.length;
		List<Integer> ans = new ArrayList<Integer>(n);
		for (int index = 0; index < nums.length; index++) {
			int count = 0;
			for (int j=index+1; j < nums.length; j++) {
				if (nums[index] > nums[j]) {
					count ++;
				}
			}
			ans.add(count);
		}
		return ans;

	}

	public static void main(String[] args) {
		int n = 50;
		int[] nums = new int[n];
		for (int i = 0; i < n; i++) {
			nums[i] = (int)(Math.random() * 15);
			System.out.print(nums[i] + ", ");
		}
		System.out.println();
		nums = new int[] {197, 69, 159, 160, 194, 192, 174, 175, 15, 86, 102, 14, 127, 60, 44, 177, 76, 64, 98, 146, 197, 121, 55, 130, 96, 104, 165, 54, 67, 151, 199, 34, 84, 18, 182, 94, 136, 118, 43, 19, 78, 180, 195, 51, 137, 104, 16, 0, 198, 55, 71, 26, 129, 31, 197, 67, 58, 171, 54, 196, 158, 23, 39, 11, 76, 25, 151, 137, 140, 187, 193, 194, 112, 180, 17, 115, 105, 74, 11, 82, 79, 16, 100, 108, 160, 175, 56, 39, 146, 88, 161, 151, 163, 55, 140, 57, 97, 13, 134, 135, 188, 183, 118, 13, 33, 65, 64, 175, 21, 83, 3, 22};
		//System.out.println(nums.length);
		Solution315 a = new Solution315();

		System.out.println(a.countSmaller(nums));
		System.out.println(a.countSmaller2(nums));
	}
}
