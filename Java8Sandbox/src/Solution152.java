import java.util.Arrays;

// leetcode #152
// https://leetcode.com/problems/maximum-product-subarray/
public class Solution152 {
    public int maxProduct(int[] nums) {
    	if (nums.length == 1) {
    		return nums[0];
    	}
    	int maxP = 0;
    	int preNegP = 0;
    	int postNegP = 0;
    	int product = 0;
    	for (int i:nums) {
    		if (i > 0) {
    			product = product==0 ? i:product*i;
    			if (product < 0) {
    				postNegP = postNegP==0? i:postNegP*i;
    			}
    		} else if (i == 0) {
    			maxP = getMax(maxP, preNegP, postNegP, product);
    			product = 0;
    			preNegP = 0;
    			postNegP = 0;
    		} else {
    			if (product > 0) {
    				preNegP = product;
    			}
    			product = product==0 ? i:product*i;
    			postNegP = 0;
    		}
    	}
    	int maxP1 = getMax(maxP, preNegP, postNegP, product);
    	// check backwards ... there is a better way to do it but might as well do this for easiness.
    	maxP = 0;
    	preNegP = 0;
    	postNegP = 0;
    	product = 0;
    	for (int a=nums.length-1; a>=0; a--) {
    		int i = nums[a];
    		if (i > 0) {
    			product = product==0 ? i:product*i;
    			if (product < 0) {
    				postNegP = postNegP==0? i:postNegP*i;
    			}
    		} else if (i == 0) {
    			maxP = getMax(maxP, preNegP, postNegP, product);
    			product = 0;
    			preNegP = 0;
    			postNegP = 0;
    		} else {
    			if (product > 0) {
    				preNegP = product;
    			}
    			product = product==0 ? i:product*i;
    			postNegP = 0;
    		}
    	}
    	int maxP2 = getMax(maxP, preNegP, postNegP, product);
        return Math.max(maxP1, maxP2);
    }

	private int getMax(int maxP, int preNegP, int postNegP, int product) {
		return Math.max(maxP, Math.max(product, Math.max(preNegP, postNegP)));
	}

	public static void main(String[] args) {
		int maxLength = 12;
		int range = 10;
		int[] d = new int[]{0, -5, 10, 5, 6, -6, -4, 7, 7, -4, -8, 4};
		Solution152 s = new Solution152();
		s.maxProduct(d);
		for (int i=0; i<50; i ++) {
			int[] nums = new int[maxLength];
			for (int j = 0; j < maxLength; j++) {
				double rand = Math.random();
				int multiplier = 1;
				if (rand < 0.1) {
					multiplier = 0;
				} else if (rand < 0.3) {
					multiplier = -1;
				}
				nums[j] = (int)(Math.random()*range + 1) * multiplier;
			}
			System.out.println(Arrays.toString(nums));

		}
	}
}
