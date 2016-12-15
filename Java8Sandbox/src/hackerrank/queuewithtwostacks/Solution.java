package hackerrank.queuewithtwostacks;

import java.util.Scanner;
import java.util.Stack;

public class Solution {
    public static void main(String[] args) {
        MyQueue<Integer> queue = new MyQueue<Integer>();

        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        for (int i = 0; i < n; i++) {
            int operation = scan.nextInt();
            if (operation == 1) { // enqueue
              queue.enqueue(scan.nextInt());
            } else if (operation == 2) { // dequeue
              queue.dequeue();
            } else if (operation == 3) { // print/peek
              System.out.println(queue.peek());
            }
        }
        scan.close();
    }
}

class MyQueue<T extends Object> {
	private Stack<T> enqueueStack = new Stack<T>();
	private Stack<T> dequeueStack = new Stack<T>();

	public void enqueue(T item) {
		enqueueStack.push(item);
	}

	public T dequeue() {
		if (dequeueStack.isEmpty()) {
			swapStack();
		}
		return dequeueStack.pop();
	}

	public T peek() {
		if (dequeueStack.isEmpty()) {
			swapStack();
		}
		return dequeueStack.peek();
	}

	private void swapStack() {
		while (!enqueueStack.isEmpty()) {
			dequeueStack.push(enqueueStack.pop());
		}

	}
}