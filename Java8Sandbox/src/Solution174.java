import java.util.Arrays;

/*
 * Leet code #174 - dungeon game: https://leetcode.com/problems/dungeon-game/
 */


public class Solution174 {
	public int calculateMinimumHP(int[][] dungeon) {
		// trace backward, from end point to starting point.
    	if (dungeon.length > 0) {
    		int rowNo = dungeon.length;
    		int colNo = dungeon[0].length;
    		int[][] hp = new int[rowNo][colNo];
    		int lastRow = rowNo-1;
			int lastCol = colNo-1;
			hp[lastRow][lastCol] = Math.min(0, dungeon[lastRow][lastCol]);
    		// calculate bottom row
    		for (int col=lastCol-1; col >=0; col--) {
    			hp[lastRow][col] = Math.min(0, dungeon[lastRow][col] + hp[lastRow][col+1]);
    		}
    		// calucluate last col
    		for (int row=lastRow-1; row >=0; row--) {
    			hp[row][lastCol] = Math.min(0, dungeon[row][lastCol] + hp[row+1][lastCol]);
    		}
    		for (int row = lastRow-1; row >= 0; row--) {
    			for (int col = lastCol-1; col>=0; col--) {
    				hp[row][col] = Math.min(0, dungeon[row][col] + Math.max(hp[row][col+1], hp[row+1][col]));
    			}
    		}
    		return hp[0][0] * -1 + 1;
    	} else {
    		return 1;
    	}
	}

	// the slow but correct way.
    public int calculateMinimumHP2(int[][] dungeon) {
    	if (dungeon.length > 0) {
    		int rowNo = dungeon.length;
    		int colNo = dungeon[0].length;
    		return searchPath(dungeon, 0, 0, 0, rowNo, colNo) * -1 + 1;
    	} else {
    		return 1;
    	}
    }


    // too slow.
	private int searchPath(int[][] dungeon, int hp, int rowIdx, int colIdx, int rowNo, int colNo) {
		if (rowIdx+1 == rowNo && colIdx+1 == colNo) {
			//System.out.println("(" + rowIdx + "," + colIdx + ") - " + dungeon[rowIdx][colIdx] );
			return Math.min(0, hp + dungeon[rowIdx][colIdx]);
		} else {
			int newHp = hp + dungeon[rowIdx][colIdx];
			//System.out.println("(" + rowIdx + "," + colIdx + ") - " + newHp + " / " + newHp);
			int rightMinHp = Integer.MIN_VALUE;
			if (rowIdx + 1 < rowNo) {
				rightMinHp = searchPath(dungeon, newHp, rowIdx+1, colIdx, rowNo, colNo);
				rightMinHp = Math.min(0, rightMinHp);
			}
			int downMinHp = Integer.MIN_VALUE;
			if (colIdx + 1 < colNo) {
				downMinHp = searchPath(dungeon, newHp, rowIdx, colIdx+1, rowNo, colNo);
				downMinHp = Math.min(0, downMinHp);
			}
			int pathLowHp = Math.max(downMinHp, rightMinHp);
			return newHp >= 0 ? pathLowHp: Math.min(newHp, pathLowHp);
		}
	}


	public static void main(String[] args) {
		int mMax = 10;
		int nMax = 10;
		int attemp = 100;
		int offset = 25;
		Solution174 s = new Solution174();
		int[][] d = new int[5][5];
//		d[0] = new int[]{  0,   0, -1};
//		d[1] = new int[]{ -1,   0, -1};
//		d[2] = new int[]{ -1,   0,  0};
		d[0] = new int[]{-9, -7, -6, 0, -5};
		d[1] = new int[]{-16, 6, -4, -8, -11};
		d[2] = new int[]{-1, -11, -2, -5, -3};
		d[3] = new int[]{-2, -3, 7, 0, 3};
		d[4] = new int[]{2, 0, 6, 3, -16};
		System.out.println(s.calculateMinimumHP(d));
		d = new int[1][1];
		d[0] = new int[]{-200};
		System.out.println(s.calculateMinimumHP(d));
		for (int i=0; i<attemp; i++) {
			int n = (int)((nMax -2) * Math.random()) + 3;
			int m = (int)((mMax -2) * Math.random()) + 3;
			int[][] dungeon = new int[m][n];
			for (int[] row: dungeon) {
				for (int j=0; j<row.length; j++) {
					row[j] = (int)((Math.random() - 0.7) * offset);
				}
			}
			int ans1 = s.calculateMinimumHP(dungeon);
			int ans2 = s.calculateMinimumHP2(dungeon);
			if (ans1 != ans2) {
				//System.out.println(concatWithCommas(dungeon) );
				System.out.println("Mismatch for happend! => " + ans1 + " vs " + ans2);
				System.out.println(concatWithCommas(dungeon) );
			}
			//System.out.println(concatWithCommas(dungeon) );
			//System.out.println(concatWithCommas(dungeon) + s.calculateMinimumHP(dungeon));
		}
		System.out.println("done");
	}

	public static String concatWithCommas(int[][] matrix) {
	    StringBuilder wordList = new StringBuilder();
	    for (int[] row : matrix) {
	        wordList.append(Arrays.toString(row) + ",");
	    }
	    return new String("[" +wordList.deleteCharAt(wordList.length() - 1) + "]");
	}
}
