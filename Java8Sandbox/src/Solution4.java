import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * 
 * @author Rays
 * https://leetcode.com/problems/median-of-two-sorted-arrays/
 * 
 * There are two sorted arrays nums1 and nums2 of size m and n respectively.
 * Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
 */


public class Solution4 {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {   	
    	boolean findAverage = (nums1.length+nums2.length)%2 == 0;
    	int expectedNumBelowLowerMedian = findAverage? 
    			(nums1.length+nums2.length)/2 - 1: (nums1.length+nums2.length-1)/2; 
    	int[] base, pivot;
    	if (nums1.length > nums2.length) {
    		base = nums1;
    		pivot = nums2;
    	} else {
    		base = nums2;
    		pivot = nums1;    		
    	}
    	// taking care of corner cases
    	if (pivot.length == 0) {
    		return findMedian(pivot, base); 
    	} else if (pivot[pivot.length-1] <= base[0]) {
    		return findMedian(pivot, base);
    	} else if (base[base.length-1] <= pivot[0]) {
    		return findMedian(base, pivot);
    	}
    	int ub = base.length -1 ;
    	int lb = 0;
    	boolean oneMediumFound = false;
    	int numBelowBaseValueOnPivot;
    	boolean zeroTried = false;
    	do {
    		int midpoint = (lb + ub) / 2;
			numBelowBaseValueOnPivot = countNumberBelowOrEqualValueByBinarySearch(pivot, base[midpoint]);
        	int numberFound = numBelowBaseValueOnPivot + midpoint; // # of numbers == or < base[midpoint]
        	if (numberFound > expectedNumBelowLowerMedian) {
        		ub = midpoint;
        	} else if (numberFound < expectedNumBelowLowerMedian){
        		lb = midpoint;
        	} else {
        		// one medium found,
        		lb = midpoint;
        		oneMediumFound = true;
        		break;
        	}
        	zeroTried = (midpoint == 0);
    	} while (ub > lb + 1 || (lb == 0 && !zeroTried));
    	int median1, median2;
    	int pIndex = -1;
    	if (oneMediumFound) {
    		median1 = base[lb];
    		if (findAverage) {
    			pIndex = countNumberBelowOrEqualValueByBinarySearch(pivot, base[lb]);
    		}
    	} else {
    		int medianIndexOnPivot = expectedNumBelowLowerMedian - (lb + 1);
    		median1 = pivot[medianIndexOnPivot];
    		if (findAverage) {
    			pIndex = medianIndexOnPivot + 1;
    		}
    	}
		if (findAverage) {
			if (pIndex < pivot.length) {
				median2 = Math.min(pivot[pIndex], base[lb+1]);
			} else {
				median2 = base[lb+1];
			}
		} else {
			median2 = median1;
		}    	
		return (median1 + median2) / 2.0;
    }

    public double findMedian(int[] sArray, int[] lArray) {
    	int medianIndex = (sArray.length+lArray.length - 1)/2;
    	int median1;
    	if (sArray.length > medianIndex) {
    		median1 = sArray[medianIndex];
    	} else {
    		median1 = lArray[medianIndex - sArray.length];
    	}
    	int median2;
    	if ((sArray.length+lArray.length) % 2 == 0) {
    		int median2Index = medianIndex + 1;
        	if (sArray.length > median2Index) {
        		median2 = sArray[median2Index];
        	} else {
        		median2 = lArray[median2Index - sArray.length];
        	}
    	} else {
    		median2 = median1;
    	}
    	return (median1 + median2) / 2.0;
    }
    
    /**
     * @param base
     * @param value
     * @return the index o
     */
    public int countNumberBelowOrEqualValueByBinarySearch(int[] base, int value) {
    	int lb = 0;
    	int ub = base.length - 1;
    	while (true) {
    		int midpoint = (lb+ub)/2;
    		//exit conditions:
    		if (value == base[midpoint]) {
    			while (midpoint+1 < base.length && value == base[midpoint+1]) {
    				midpoint ++;
    			}
    			return midpoint+1;
    		} else if (midpoint == lb) {
    			if (base[ub] <= value) {
    				return ub+1; // 0 indexed
    			} else if(base[lb] > value) {
    				return 0;
    			} else {
    				return lb+1;
    			}
    		}
			if (value > base[midpoint]) {
    			lb = midpoint;
    		} else if(value < base[midpoint]) {
    			ub = midpoint;
    		}
    	}
    }
    
    public static int[] generateRandomIntArray(int size) {
    	List<Integer> a = new ArrayList<Integer>();
    	for (int i=0; i<size; i++) {
    		a.add(new Integer((int)(Math.random()*1000)));
    	}
    	Collections.sort(a);
    	int[] returnArray = convertToIntArray(a);
    	return returnArray;
    }

	private static int[] convertToIntArray(List<Integer> a) {
		int[] returnArray = new int[a.size()];
    	for (int i=0; i<a.size(); i++) {
    		returnArray[i] = a.get(i);
    	}
		return returnArray;
	}
    
    public static void main(String[] args) {
    	Solution4 sol = new Solution4();
    	System.out.println(sol.findMedianSortedArrays(new int[]{38, 252, 474, 494, 704}, new int[]{511, 537, 637, 677, 734}) == 524);
    	System.out.println(sol.findMedianSortedArrays(new int[]{207, 753}, new int[]{288, 427}) == 357.5);
    	System.out.println(sol.findMedianSortedArrays(new int[]{771}, new int[]{173}) == 472.0);
    	System.out.println(sol.findMedianSortedArrays(new int[]{1, 1}, new int[]{1}) == 1.0);
    	System.out.println(sol.findMedianSortedArrays(new int[]{2, 2}, new int[]{2}) == 2.0);
    	System.out.println(sol.findMedianSortedArrays(new int[]{1, 2, 3, 4}, new int[]{5, 6, 7}) == 4.0);
    	System.out.println(sol.findMedianSortedArrays(new int[]{4, 5, 6, 7}, new int[]{1, 2, 3}) == 4.0); 
    	System.out.println(sol.findMedianSortedArrays(new int[]{1, 2, 2, 3}, new int[]{0, 1, 2, 3, 4}) == 2.0); //2
    	System.out.println(sol.findMedianSortedArrays(new int[]{}, new int[]{1, 3}) == 2.0); //2
    	System.out.println(sol.findMedianSortedArrays(new int[]{6, 8}, new int[]{1, 3, 5, 7, 9}) == 6.0); 
    	System.out.println(sol.findMedianSortedArrays(new int[]{8, 10}, new int[]{1, 3, 5, 7, 9}) == 7.0);
    	System.out.println(sol.findMedianSortedArrays(new int[]{140, 144, 221, 391, 400, 543, 564, 610, 686, 700, 987}, new int[]{205, 271, 386, 473, 805, 944, 971}) == 508.0);
    	int run = 1000;
    	for (int i = 0; i<run; i++) {
    		int size = (int) (Math.random() * 20) + 2;
    		int[] array = generateRandomIntArray(size);
    		int mid = (size - 1) / 2;
    		double median = size%2==0 ? (array[mid] + array[mid+1])/2.0 : array[mid];
			List<Integer> a1 = new ArrayList<Integer>();
			List<Integer> a2 = new ArrayList<Integer>();
			double splitRate = Math.random();
			for (int j = 0; j < size; j++) {
				if (Math.random() > splitRate) {
					a1.add(array[j]);
				} else {
					a2.add(array[j]);
				}
    		}
			if (median != sol.findMedianSortedArrays(convertToIntArray(a1), convertToIntArray(a2))) {
				System.out.println("ERROR on");
				System.out.println("a1 = " + a1);
				System.out.println("a2 = " + a2);
				System.out.println("Median = " + median + " calculated median = " + sol.findMedianSortedArrays(convertToIntArray(a1), convertToIntArray(a2)));
			}
    	}
    	System.out.println("FINISHED");
    }
}