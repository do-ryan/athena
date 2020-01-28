"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_fwd = []
        self.stack_bck = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.stack_fwd and self.stack_bck:
            while self.stack_bck:
                self.stack_fwd.append(self.stack_bck.pop(-1))
        self.stack_fwd.append(x) # push x to stack fwd

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack_bck and self.stack_fwd:
            while self.stack_fwd:
                self.stack_bck.append(self.stack_fwd.pop(-1))
        return self.stack_bck.pop(-1)

    def peek(self) -> int:
        """
        Get the front element.
        """
        ret = self.pop()
        self.stack_bck.append(ret)
        return ret

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack_fwd and not self.stack_bck



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
