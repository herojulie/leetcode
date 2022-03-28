# # Code for Min Heap
# import heapq
#
# # Create an array
# minHeap = []
#
# # Heapify the array into a Min Heap
# heapq.heapify(minHeap)
#
# # Add 3，1，2 respectively to the Min Heap
# heapq.heappush(minHeap, 3)
# heapq.heappush(minHeap, 1)
# heapq.heappush(minHeap, 2)
#
# # Check all elements in the Min Heap, the result is [1, 3, 2]
# print("minHeap: ", minHeap)
#
# # Get the top element of the Min Heap
# peekNum = minHeap[0]
#
# # The result is 1
# print("peek number: ", peekNum)
#
# # Delete the top element in the Min Heap
# popNum = heapq.heappop(minHeap)
#
# # The result is 1
# print("pop number: ", popNum)
#
# # Check the top element after deleting 1, the result is 2
# print("peek number: ", minHeap[0])
#
# # Check all elements in the Min Heap, the result is [2,3]
# print("minHeap: ", minHeap)
#
# # Check the number of elements in the Min Heap
# # Which is also the length of the Min Heap
# size = len(minHeap)
#
# # The result is 2
# print("minHeap size: ", size)

# Code for Min Heap
import heapq

# Create an array
min_heap = []

# Heapify the array into a Min Heap
heapq.heapify(min_heap)

# Add 3，1，2 respectively to the Min Heap
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 2)

# Check all elements in the Min Heap, the result is [1, 3, 2]
print("min heap=", min_heap)

# Get the top element of the Min Heap
peek_num = min_heap[0]

# The result is 1
print(peek_num)

# Delete the top element in the Min Heap
del_num = heapq.heappop(min_heap)

# The result is 1
print(del_num)

# Check the top element after deleting 1, the result is 2
print(min_heap[0])

# Check all elements in the Min Heap, the result is [2,3]
print(min_heap)

# Check the number of elements in the Min Heap
# Which is also the length of the Min Heap
print(len(min_heap))

# The result is 2
