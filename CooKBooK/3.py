# cook book bilan ishlaymiz
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
import heapq

heap = list(nums)
print(f"{heap}, {type(heap)}")
heapq.heapify(heap)
print(heap)
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(nums[:3])  # boshidan 3 ta chiqaradi
print(nums[-3:])  # ohiradan 3 ta chiqaradi
print(sorted(nums)[:3])
print(sorted(nums)[-3:])
# 23 12 2024