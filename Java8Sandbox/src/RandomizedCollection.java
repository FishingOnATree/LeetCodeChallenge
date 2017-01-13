import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

// Leetcode #381: https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
public class RandomizedCollection {
	private Map<Integer, Set<Integer>> map;
	private List<Integer> list;

    /** Initialize your data structure here. */
    public RandomizedCollection() {
        map = new HashMap<Integer, Set<Integer>>(1000);
        list = new ArrayList<Integer>(1000);
    }

    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    public boolean insert(int val) {
    	boolean returnValue = !map.containsKey(val);
    	list.add(val);
    	Set<Integer> indexSet = map.get(val);
    	if (indexSet == null) {
    		indexSet = new HashSet<Integer>();
    		map.put(val, indexSet);
    	}
    	indexSet.add(list.size()-1);
    	return returnValue;
    }

    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    public boolean remove(int val) {
    	if (map.containsKey(val)) {
    		Set<Integer> indexSet = map.get(val);
    		int lastIndex = list.size() - 1;
    		int lastNum = list.get(lastIndex);
    		list.remove(lastIndex);
    		if (lastNum == val) {
    			indexSet.remove(lastIndex);
    		} else {
        		int index = indexSet.iterator().next().intValue();
        		list.set(index, lastNum);
        		map.get(lastNum).remove(lastIndex);
        		map.get(lastNum).add(index);
        		indexSet.remove(index);
    		}
    		if (indexSet.isEmpty()) {
    			map.remove(val);
    		}
    		return true;
    	} else {
    		return false;
    	}
    }

    /** Get a random element from the collection. */
    public int getRandom() {
    	if (list.isEmpty()) {
    		return -1;
    	} else {
    		return list.get((int)(Math.random()*list.size()));
    	}
    }

    public static void main(String[] args) {
    	int max = 10000;
    	int maxValue = 500;
//    	String[] s = new String[]{"remove","getRandom","getRandom","insert","remove","getRandom","insert","insert","getRandom","insert","remove","insert","remove","getRandom","insert","insert","getRandom","getRandom","insert","insert","getRandom","remove","remove","getRandom","remove","getRandom","remove","insert","getRandom","getRandom","getRandom","insert","insert","insert","getRandom","remove","insert","getRandom","insert","getRandom","remove","getRandom","remove","insert","remove","insert","getRandom","remove","insert","remove","getRandom","insert","getRandom","getRandom","insert","remove","insert","remove","remove","remove","getRandom","insert","getRandom","insert","remove","getRandom","remove","remove","insert","remove","insert","remove","insert","insert","getRandom","insert","getRandom","remove","getRandom","getRandom","getRandom","insert","insert","insert","insert","insert","getRandom","insert","insert","getRandom","remove","getRandom","insert","remove","remove","remove","insert","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","insert","getRandom","remove","remove","insert","remove","remove","insert","remove","insert","getRandom","insert","insert","remove","getRandom","getRandom","getRandom","insert","getRandom","remove","getRandom","getRandom","getRandom","getRandom","insert","getRandom","insert","insert","insert","insert","remove","insert","remove","remove","remove","remove","insert","getRandom","remove","getRandom","remove","remove","insert","insert","getRandom","remove","insert","getRandom","remove","getRandom","insert","insert","remove","getRandom","insert","remove","insert","remove","insert","getRandom","getRandom","insert","insert","remove","getRandom","getRandom","insert","getRandom","remove","remove","insert","insert","remove","remove","getRandom","insert","remove","getRandom","insert","insert","insert","insert","insert","remove","remove","getRandom","getRandom","getRandom","insert","getRandom","getRandom","insert","remove","insert","getRandom","remove","remove","insert","insert","getRandom","insert","getRandom","insert","remove","insert","getRandom","remove","getRandom","insert","getRandom","insert","insert","remove","remove","insert","insert","remove","remove","insert","insert","getRandom","remove","insert","remove","getRandom","remove","remove","remove","remove","getRandom","getRandom","remove","insert","getRandom","getRandom","remove","getRandom","insert","getRandom","insert","getRandom","getRandom","insert","remove","insert","remove","getRandom","remove","getRandom","getRandom","getRandom","getRandom","getRandom","insert","remove","insert","remove","insert","insert","remove","remove","remove","getRandom","getRandom","insert","remove","remove","getRandom","getRandom","insert","getRandom","remove","insert","getRandom","getRandom","remove","getRandom","getRandom","getRandom","insert","insert","insert","insert","remove","remove","insert","insert","remove","getRandom","getRandom","insert","remove","remove","remove","insert","insert","insert","remove","getRandom","remove","insert","remove","insert","remove","insert","remove","insert","getRandom","insert","remove","remove","insert","remove","getRandom","insert","remove","remove","insert","insert","remove","insert","insert","remove","insert","remove","getRandom","remove","insert","insert","remove","getRandom","getRandom","remove","remove","remove","getRandom","insert","insert","remove","remove","insert","insert","insert","insert","insert","insert","getRandom","getRandom","getRandom","remove","remove","getRandom","getRandom","insert","remove","remove","insert","insert","insert","remove","getRandom","insert","getRandom","getRandom","insert","insert","getRandom","insert","getRandom","getRandom","getRandom","getRandom","getRandom","remove","remove","insert","remove","getRandom","remove","remove","remove","remove","remove","getRandom","insert","insert","getRandom","getRandom","remove","insert","remove","getRandom","insert","insert","getRandom","insert","getRandom","remove","getRandom","insert","getRandom","insert","insert","getRandom","insert","remove","getRandom","remove","insert","remove","remove","insert","remove","remove","getRandom","remove","getRandom","insert","remove","insert","insert","getRandom","getRandom","remove","getRandom","getRandom","insert","insert","remove","insert","insert","remove","insert","insert","getRandom","getRandom","getRandom","insert","remove","getRandom","getRandom","insert","getRandom","getRandom","remove","getRandom","remove","remove","getRandom","remove","insert","insert","remove","insert","remove","remove","getRandom","insert","getRandom","remove","remove","remove","insert","insert","getRandom","remove","remove","getRandom","getRandom","getRandom","remove","remove","remove","getRandom","insert","getRandom","insert","remove","remove","insert","insert","remove","remove","getRandom","getRandom","remove","remove","getRandom","getRandom","remove","remove","remove","remove","remove","getRandom","insert","remove","getRandom","getRandom","insert","remove","insert","getRandom","remove","remove","remove","remove","remove","insert","remove","remove","getRandom","insert","remove","insert","insert","remove","remove","getRandom","getRandom","remove","insert","getRandom","insert","insert","getRandom","remove","getRandom","remove","remove","remove","remove","insert","remove","remove","getRandom","getRandom","insert","remove","insert","getRandom","getRandom","remove","getRandom","remove","remove","insert","remove","insert","insert","insert","remove","insert","getRandom","remove","insert","insert","getRandom","remove","remove","insert","insert","getRandom","remove","insert","insert","getRandom","remove","remove","getRandom","getRandom","remove","insert","insert","remove","insert","getRandom","remove","insert","remove","remove","insert","getRandom","remove","remove","insert","remove","insert","remove","remove","insert","getRandom","remove","remove","insert","insert","remove","insert","insert","remove","remove","getRandom","remove","getRandom","getRandom","insert","remove","remove","getRandom","getRandom","insert","remove","getRandom","remove","getRandom","remove","insert","getRandom","insert","getRandom","remove","getRandom","remove","remove","remove","insert","remove","getRandom","remove","getRandom","remove","remove","insert","insert","getRandom","remove","insert","insert","getRandom","getRandom","insert","getRandom","insert","insert","getRandom","remove","getRandom","getRandom","remove","insert","getRandom","remove","remove","insert","getRandom","remove","remove","insert","remove","insert","getRandom","remove","getRandom","insert","remove","insert","insert","getRandom","remove","getRandom","getRandom","remove","getRandom","getRandom","remove","remove","insert","remove","insert","getRandom","remove","remove","remove","insert","remove","getRandom","insert","remove","getRandom","insert","getRandom","insert","getRandom","getRandom","remove","insert","insert","insert","insert","remove","getRandom","getRandom","remove","remove","remove","getRandom","remove","insert","remove","insert","getRandom","remove","insert","getRandom","insert","getRandom","remove","insert","insert","insert","remove","remove","getRandom","remove","getRandom","remove","getRandom","remove","remove","remove","getRandom","remove","getRandom","getRandom","getRandom","insert","getRandom","getRandom","insert","getRandom","remove","getRandom","insert","getRandom","remove","remove","insert","remove","remove","getRandom","remove","remove","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","remove","insert","getRandom","insert","insert","remove","insert","getRandom","remove","insert","getRandom","getRandom","insert","insert","getRandom","remove","insert","remove","insert","getRandom","insert","remove","insert","insert","remove","remove","insert","remove","remove","insert","getRandom","insert","remove","getRandom","remove","getRandom","getRandom","insert","remove","remove","getRandom","insert","remove","getRandom","getRandom","getRandom","getRandom","getRandom","remove","remove","getRandom","remove","insert","getRandom","insert","getRandom","insert","insert","getRandom","remove","insert","remove","getRandom","remove","insert","remove","insert","getRandom","insert","insert","getRandom","remove","getRandom","getRandom","remove","remove","remove","getRandom","getRandom","insert","remove","getRandom","remove","insert","remove","remove","getRandom","getRandom","remove","remove","getRandom","insert","getRandom","getRandom","getRandom","remove","getRandom","insert","getRandom","insert","remove","insert","getRandom","getRandom","remove","remove","getRandom","remove","insert","remove","insert","getRandom","remove","getRandom","insert","insert","remove","remove","remove","getRandom","getRandom","remove","insert","insert","remove","insert","insert","remove","getRandom","remove","remove","getRandom","getRandom","getRandom","getRandom","insert","insert","remove","getRandom","remove","insert","remove","getRandom","remove","insert","insert","remove","getRandom","getRandom","insert","insert","insert","insert","remove","remove","getRandom","insert","insert","insert","insert","insert","remove","getRandom","insert","remove","remove","remove","insert","insert","insert","remove","remove","insert","insert","insert","remove","insert","remove","remove","remove","insert","insert","remove","remove","getRandom","getRandom","remove","remove","remove","insert","getRandom","getRandom","remove","remove","getRandom","getRandom","insert","insert","insert","insert","remove","remove","insert","remove","remove","getRandom","remove","remove","insert","insert","remove","remove","insert","insert","getRandom","getRandom","remove","getRandom","insert","remove","insert","remove","insert","remove","insert","insert","insert","getRandom","getRandom","getRandom","insert","remove","getRandom","getRandom","remove","getRandom","insert","remove","insert"};
//    	int[] vals = new int[]{216, 114, 14, 370, 120, 268, 323, 111, 432, 51, 231, 383, 435, 205, 419, 124, 479, 87, 311, 438, 124, 447, 29, 407, 360, 284, 85, 40, 256, 444, 238, 73, 32, 204, 58, 446, 157, 257, 369, 418, 222, 100, 382, 389, 430, 469, 432, 151, 213, 104, 363, 373, 67, 213, 250, 310, 351, 171, 243, 277, 411, 90, 470, 123, 16, 21, 27, 24, 211, 201, 254, 48, 328, 334, 81, 73, 23, 71, 364, 267, 309, 449, 275, 461, 210, 182, 408, 358, 271, 315, 401, 173, 279, 398, 2, 406, 182, 437, 127, 67, 327, 11, 79, 318, 240, 88, 233, 117, 320, 163, 110, 55, 427, 6, 382, 225, 475, 394, 491, 76, 277, 357, 175, 337, 485, 75, 326, 203, 125, 193, 234, 133, 340, 455, 377, 189, 64, 161, 74, 27, 498, 100, 415, 215, 380, 221, 8, 233, 142, 443, 241, 86, 209, 105, 329, 142, 292, 223, 98, 359, 160, 291, 30, 271, 10, 49, 259, 163, 161, 215, 310, 18, 445, 334, 9, 459, 274, 0, 107, 486, 487, 364, 296, 491, 237, 421, 417, 119, 250, 239, 281, 173, 467, 386, 148, 410, 163, 446, 53, 167, 291, 159, 253, 409, 403, 301, 249, 398, 145, 94, 400, 311, 424, 27, 334, 267, 495, 109, 424, 347, 327, 199, 286, 293, 225, 174, 311, 246, 335, 330, 443, 448, 252, 43, 468, 10, 106, 316, 258, 437, 105, 493, 21, 250, 145, 25, 207, 155, 230, 311, 403, 340, 58, 252, 111, 102, 262, 285, 472, 139, 411, 302, 114, 465, 21, 447, 408, 15, 423, 459, 71, 160, 477, 315, 152, 450, 260, 68, 89, 51, 434, 395, 120, 445, 181, 7, 483, 110, 185, 174, 454, 498, 264, 275, 386, 273, 395, 373, 60, 394, 495, 468, 267, 228, 442, 198, 169, 57, 442, 369, 110, 395, 491, 345, 190, 225, 278, 429, 499, 348, 29, 9, 94, 175, 397, 363, 361, 421, 128, 135, 81, 277, 382, 130, 119, 262, 173, 187, 278, 102, 61, 38, 2, 65, 315, 153, 222, 354, 417, 225, 264, 252, 394, 62, 379, 355, 84, 269, 59, 338, 78, 251, 441, 353, 195, 171, 227, 239, 480, 131, 159, 395, 329, 472, 236, 265, 491, 207, 459, 6, 293, 237, 36, 60, 85, 103, 92, 444, 10, 180, 63, 225, 342, 330, 64, 256, 246, 146, 163, 378, 450, 67, 106, 413, 439, 243, 164, 415, 415, 187, 415, 248, 366, 332, 360, 200, 254, 286, 446, 464, 412, 154, 155, 445, 401, 465, 467, 456, 181, 331, 111, 36, 86, 115, 164, 194, 207, 495, 160, 45, 435, 449, 20, 426, 4, 292, 217, 178, 42, 44, 231, 442, 219, 15, 460, 415, 256, 126, 400, 150, 125, 113, 6, 96, 449, 367, 276, 224, 211, 327, 259, 183, 493, 421, 257, 60, 124, 205, 159, 473, 215, 476, 450, 296, 194, 237, 84, 497, 73, 47, 492, 153, 319, 379, 174, 355, 299, 277, 417, 332, 432, 189, 300, 244, 263, 490, 306, 233, 328, 356, 448, 427, 311, 239, 464, 235, 72, 342, 259, 386, 321, 115, 383, 288, 265, 409, 479, 420, 234, 55, 241, 75, 397, 270, 66, 427, 293, 396, 182, 482, 51, 119, 204, 133, 274, 440, 128, 141, 204, 285, 477, 3, 414, 269, 372, 278, 364, 267, 454, 93, 331, 51, 217, 133, 314, 389, 421, 97, 148, 118, 377, 187, 197, 343, 38, 327, 99, 26, 433, 463, 195, 347, 138, 383, 350, 379, 55, 135, 57, 188, 448, 267, 289, 154, 269, 198, 220, 388, 457, 184, 46, 270, 0, 463, 278, 249, 197, 279, 474, 170, 151, 109, 45, 26, 184, 69, 352, 147, 465, 49, 465, 473, 267, 313, 66, 174, 423, 365, 115, 17, 129, 66, 2, 488, 417, 53, 59, 315, 203, 183, 414, 171, 467, 334, 291, 427, 245, 2, 12, 492, 212, 285, 31, 377, 311, 470, 23, 241, 439, 23, 108, 333, 400, 467, 466, 320, 395, 212, 197, 170, 495, 49, 407, 335, 130, 133, 148, 151, 274, 407, 426, 442, 127, 67, 160, 0, 215, 241, 61, 190, 459, 244, 52, 82, 377, 340, 468, 122, 237, 105, 380, 482, 68, 93, 56, 373, 84, 128, 146, 189, 194, 192, 340, 23, 398, 470, 360, 177, 495, 277, 265, 451, 143, 176, 192, 96, 456, 265, 252, 440, 428, 194, 469, 353, 114, 124, 213, 286, 115, 464, 273, 311, 34, 330, 285, 154, 215, 315, 380, 372, 180, 271, 44, 446, 311, 431, 296, 179, 460, 335, 425, 411, 272, 128, 140, 204, 164, 441, 126, 259, 489, 194, 119, 454, 71, 255, 224, 32, 408, 53, 356, 63, 461, 348, 269, 472, 86, 478, 306, 1, 280, 47, 89, 142, 34, 134, 21, 170, 225, 220, 77, 51, 92, 176, 9, 118, 472, 251, 188, 27, 88, 161, 446, 139, 325, 457, 417, 96, 30, 32, 470, 488, 18, 195, 488, 112, 83, 411, 336, 489, 426, 405, 22, 386, 74, 455, 152, 253, 431, 343, 417, 71, 288, 29, 474, 284, 200, 260, 209, 46, 287, 446, 489, 211, 124, 257, 146, 55, 26, 16, 44, 392, 155, 97, 232, 343, 486, 162, 273, 148, 314, 188, 2, 49, 103, 354, 70, 374, 95, 21, 253, 100, 227, 100, 153, 278, 37, 290, 6, 353, 357, 256, 481, 495, 200, 448, 438, 244, 422, 402, 263, 327, 297, 463, 28, 187, 333, 29, 309, 363, 237, 2, 182, 474, 78, 293, 483, 225, 330, 316, 76, 426, 90, 80, 499, 188, 390, 50, 461, 51, 160, 139, 311, 435, 7, 259, 207, 449, 121, 31, 355, 175, 218, 349, 298, 219, 77, 132, 374, 403, 345, 217, 63, 125, 406, 468, 105, 28, 236, 326, 366, 250, 301, 97, 51, 131, 162, 470, 28, 419, 92, 315, 97, 96, 128, 482, 209, 108, 102, 427, 232, 376, 338, 122, 18, 119, 289, 325, 109, 127, 71, 418, 91, 246, 414, 142, 198, 477, 215, 185};
    	String[] s = new String[max];
    	int[] vals = new int[max];
    	for (int i=0; i<s.length; i++) {
    		double seed = Math.random();
    		int num = (int)(Math.random()*maxValue);
    		if (seed < 0.35) {
    			s[i] = "insert";
    		} else if (seed < 0.7) {
    			s[i] = "remove";
    		} else {
    			s[i] = "getRandom";
    		}
    		vals[i] = num;
    	}
    	try {
	    	RandomizedCollection c = new RandomizedCollection();
	    	for (int i=0; i<s.length; i++) {
	    		System.out.println(i);
	    		int num = vals[i];
	    		if (s[i].equals("insert")) {
	    			c.insert(num);
	    		} else if (s[i].equals("remove")) {
	    			c.remove(num);
	    		} else if (s[i].equals("getRandom")) {
	    			c.getRandom();
	    		}
	    	}
    	} catch(Exception e) {
    		e.printStackTrace();
    		System.out.println(Arrays.toString(s));
    		System.out.println(Arrays.toString(vals));
    	}
    	System.out.println("done");
//    	c.insert(1);
//    	c.insert(1);
//    	c.insert(2);
//    	System.out.println(c.getRandom());
//    	c.remove(2);
//    	System.out.println(c.getRandom());
//    	System.out.println("");

    }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection obj = new RandomizedCollection();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */