/**
 * https://leetcode.com/problems/search-a-2d-matrix-ii/
 * @author Rays
 *
 */
public class Solution240 {
    public boolean searchMatrix(int[][] matrix, int target) {
    	int m = matrix.length;
    	int n = 0;
    	if (m > 0) {
    		n = matrix[0].length;
    	}
    	if (m == 0 || n == 0) {
    		return false;
    	}
    	return searchMatrix(matrix, target, m-1, 0, n-1, 0);
    }

	private boolean searchMatrix(int[][] matrix, int target, int rowMax, int rowMin, int colMax, int colMin) {
		if (colMax < colMin || rowMax < rowMin ||
			(target < matrix[rowMin][colMin] || target > matrix[rowMax][colMax])) {
    		return false;
    	} else if (colMax - colMin + rowMax - rowMin <= 4) {
    		for (int i = rowMin; i<= rowMax; i++) {
    			for (int j = colMin; j <= colMax; j++) {
    				if (matrix[i][j] == target) {
    					return true;
    				}
    			}
    		}
			return false;
    	} else {
    		int row = rowMax, col = colMax;
    		while (matrix[row][col] > target && row > rowMin && col > colMin) {
    			row--;
    			col--;
    		}
			boolean result = false;
    		if (matrix[row][col] == target) {
    			result = true;
    		} else if (matrix[row][col] < target){
    			// matrix[row][col] < target && matrix[row+1][col+1] > target
    			if (col + 1 <= colMax) {
    				result = searchMatrix(matrix, target, row, rowMin, colMax, col+1);
    			}
    			if (!result) {
    				// search to the right of matrix[row+1][col+1]
	    			if (row + 1 <= rowMax) {
	    				result = searchMatrix(matrix, target, rowMax, row+1, col, colMin);
	    			}
    			}
    		} else {
    			// on the matrix above or to the left
    			if (row == rowMin) { // check left matrix
    				result = searchMatrix(matrix, target, rowMax, rowMin, col - 1, colMin);
    			} else if (col == colMin) {
    				result = searchMatrix(matrix, target, row - 1, rowMin, colMax, colMin);
    			}
    		}
    		return result;
    	}
	}

    public boolean searchMatrixDumb(int[][] matrix, int target) {
    	for (int i = 0; i < matrix.length; i++) {
    		for (int j = 0; j < matrix[i].length; j++) {
    			if (matrix[i][j] == target) {
    				return true;
    			}
    		}
    	}
    	return false;
    }

    public static int[][] generateMatrix(int m, int n) {
    	int[][] matrix = new int[m][n];

    	for (int i=0; i<m; i++) {
    		for (int j=0; j<n; j++) {
    			int base = 0;
        		if (i > 0) {
        			base = matrix[i-1][j];
        		}
        		if (j > 0) {
        			base = Math.max(base, matrix[i][j-1]);
        		}
        		matrix[i][j] = base + (int)(Math.random() * 10);
    		}
    	}
    	return matrix;
    }

    public static void main(String[] args) {
    	Solution240 a = new Solution240();
    	int[][] matrix;
    	int test = 1000;
    	for (int i=0; i<test; i++) {
    		int m = (int)(Math.random() * 8) + 1;
    		int n = (int)(Math.random() * 8) + 1;
    		matrix = generateMatrix(m, n);
    		int target = matrix[0][0] + (int)((matrix[m-1][n-1] - matrix[0][0]) * Math.random());
    		validate(a, i, m, n, matrix, target);
    	}
    	System.out.print("FINSHED");
    }

	private static void validate(Solution240 a, int i, int m, int n, int[][] matrix, int target) {
		try {
			if (a.searchMatrix(matrix, target) != a.searchMatrixDumb(matrix, target)) {
				printErrorInformation(a, i, m, n, matrix, target);
			}
		} catch (Exception e) {
			// for debug purpose
			e.printStackTrace();
		}
	}

	private static void printErrorInformation(Solution240 a, int i, int m, int n, int[][] matrix, int target) {
		System.out.println();
		System.out.println("====== (" + i + ") m/n: " + m + "/" + n + " =====" );
		System.out.println("target = " + target);
		for (int j=0; j<m; j++) {
			for (int k=0; k<n; k++) {
				System.out.print(matrix[j][k] + ", ");
			}
			System.out.println();
		}
		System.out.println("a.searchMatrixDumb(matrix, target) = " + a.searchMatrixDumb(matrix, target));
	}
}



