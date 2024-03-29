# Complete Binary Tree
# O(log2n)
import heapq


def heapsort(iterable):
    """
    내림차 순 힙 정렬(Heap Sort)
    Root Node is maximum
    """
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
# [9,8,7,6,5,4,3,2,1,0]
