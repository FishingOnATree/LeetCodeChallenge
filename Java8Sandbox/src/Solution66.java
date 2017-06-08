public class Solution66 {
    public int[] plusOne(int[] digits) {
    	boolean carryOver = false;
    	int[] array = new int[digits.length];
    	digits[digits.length-1] += 1;
    	for (int i=digits.length - 1; i >= 0; i--) {
    		int newNum = (carryOver ? 1 : 0) + digits[i];
    		carryOver = (newNum / 10) > 0 ;
    		array[i] = newNum % 10;
    		// if modify in place, we can return anytime carryOver = false.
    	}
    	if (carryOver) {
    		int[] tempArray = array;
    		array = new int[array.length + 1];
    		array[0] = 1;
    		for (int i=0; i<tempArray.length; i++) {
    			array[i+1] = tempArray[i];
    		}
    	}
    	return array;
    }


    public static void main(String[] args) {
    	int max = 100000;
    	int ranInt;
    	int[] ranIntInArray;
    	Solution66 sol = new Solution66();
    	for (int i=0; i<max; i++) {
    		ranInt = i;
    		ranIntInArray = convertToArray(ranInt);
    		if (ranInt + 1 != convertToNum(sol.plusOne(ranIntInArray))) {
    			System.out.println(ranInt + " / " + convertToNum(sol.plusOne(ranIntInArray)));
    		}
    	}
    	System.out.println("done");
    }


	private static int[] convertToArray(int ranInt) {
		String intString = Integer.toString(ranInt);
		int[] array = new int[intString.length()];
		for (int i =0; i<intString.length(); i++) {
			array[i] = Integer.parseInt(intString.substring(i, i+1));
		}
		return array;
	}

	private static int convertToNum(int[] digits) {
		int num = 0;
		for (int i =0; i<digits.length; i++) {
			num = num * 10 + digits[i];
		}
		return num;
	}
}
