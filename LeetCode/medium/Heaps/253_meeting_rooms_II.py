'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''

from typing import List

class Solution:
    def minHeapify(self, arr, i):
        l, r = (i+1)*2-1, (i+1)*2
        if l <= len(arr)-1 and arr[l] < arr[i]:
            smallest = l
        else:
            smallest = i
        if r <= len(arr)-1 and arr[r] < arr[smallest]:
            smallest = r
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.minHeapify(arr, smallest)
    def createMinHeap(self, arr: List):
        for i in range (len(arr) //2-1, -1, -1):
            self.minHeapify(arr, i)
        return arr
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        start_times, end_times = [], []
        for meeting in intervals:
            start_times.append(meeting[0])
            end_times.append(meeting[1])
        start_times, end_times = self.createMinHeap(start_times), self.createMinHeap(end_times)

        rooms_occupied = 0
        max_rooms = 0
        while True:
            if len(end_times) and len(start_times) == 0:
                break
            elif start_times[0] < end_times[0] or len(end_times) == 0:
                rooms_occupied += 1
                max_rooms = max(max_rooms, rooms_occupied)

                if len(start_times) == 1:
                    start_times.pop()
                else:
                    start_times[0] = start_times.pop()
                    self.minHeapify(start_times, 0)
            else:
                rooms_occupied -= 1
                if len(end_times) == 1:
                    end_times.pop()
                else:
                    end_times[0] = end_times.pop()
                    self.minHeapify(end_times, 0)
        return max_rooms                   

