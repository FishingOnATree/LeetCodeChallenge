package hackerrank.balancedbracket;

import java.util.EmptyStackException;
import java.util.Scanner;
import java.util.Stack;

public class Solution {

    public static boolean isBalanced(String expression) {
        Stack<Character> stack = new Stack<Character>();
        for (Character c: expression.toCharArray()) {
        	if (c == '[' || c == '{' || c == '(') {
        		stack.push(c);
        	} else if (c == ']' || c == '}' || c == ')') {
        		try {
        			Character poped = stack.pop();
        			if (poped.charValue() == '[') {
        				if (c != ']')
        					return false;
        			} else if (poped.charValue() == '{') {
        				if (c != '}')
        					return false;
        			} else {
        				if (c != ')')
        					return false;
        			}
        		} catch (EmptyStackException e) {
        			return false;
        		}
        	}
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for (int a0 = 0; a0 < t; a0++) {
            String expression = in.next();
            System.out.println( (isBalanced(expression)) ? "YES" : "NO" );
        }
    }
}