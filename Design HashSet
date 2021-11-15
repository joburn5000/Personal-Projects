/*
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

- void add(key) Inserts the value key into the HashSet.
- bool contains(key) Returns whether the value key exists in the HashSet or not.
- void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.


Completed: September 1, 2021
*/

class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = []
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if (key in self.set) == False:
            self.set.append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if (key in self.set):
            self.set.remove(key)
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if key in self.set:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
