'''
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
'''
from collections import defaultdict
from random import random
import math

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.this = defaultdict(bool)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if not self.this[val]:
            self.this[val] = True
            return True
        else:
            return False


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if self.this[val]:
            self.this[val] = False
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        while True:
            val = list(self.this.keys())[math.floor(random()*len(self.this))]
            if self.this[val]:
                break
        return val
