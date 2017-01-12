import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


// Leetcode #380, https://leetcode.com/problems/insert-delete-getrandom-o1/
public class RandomizedSet {
	private Map<Integer, Integer> map;
	private List<Integer> list;

    /** Initialize your data structure here. */
    public RandomizedSet() {
        map = new HashMap<Integer,Integer>(1000);
        list = new ArrayList<Integer>(1000);
    }

    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {
    	if (map.containsKey(val)) {
    		return false;
    	} else {
    		list.add(val);
    		map.put(val, list.size()-1);
    		return true;
    	}
    }

    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {
    	if (map.containsKey(val)) {
    		int index = map.get(val);
    		int lastNum = list.get(list.size() - 1);
    		list.set(index, lastNum);
    		map.put(lastNum, index);
    		map.remove(val);
    		list.remove(list.size() - 1);
    		return true;
    	} else {
    		return false;
    	}
    }

    /** Get a random element from the set. */
    public int getRandom() {
    	if (list.isEmpty()) {
    		return -1;
    	} else {
    		return list.get((int)(Math.random()*list.size()));
    	}
    }


    public static void main(String[] args) {
    	RandomizedSet randomSet = new RandomizedSet();
    	randomSet.insert(0);
    	randomSet.insert(1);
    	randomSet.remove(0);
    	randomSet.insert(2);
    	randomSet.remove(1);
//    	int max = 1000;
//    	int attempts = 100;
//    	int[] count = new int[max];
//    	System.out.println(randomSet.getRandom());
//    	System.out.println(randomSet.getRandom());
//		for (int i=0; i<max; i++) {
//    		if (!randomSet.insert(i)) {
//    			System.out.print("Insert " + i + " failed");
//    		}
//    	}
//		assert(false);
//    	for (int i=0; i<max; i++) {
//    		if (randomSet.insert(i)) {
//    			System.out.print("Insert " + i + " worked");
//    		}
//    	}
//    	for (int i=1; i<=max*attempts; i++) {
//    		count[randomSet.getRandom()]++;
//    	}
//    	for (int i=0; i<max; i++) {
//    		if (count[i] > attempts * 1.5 || count[i] < attempts * 0.5) {
//    			System.out.println(i + " is at " + count[i]);
//    		}
//    	}
//    	System.out.println("done");
    }
}


/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */