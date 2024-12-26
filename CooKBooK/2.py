# # berilgan enng katta sonlarni topish
import heapq

nums = [1,8,2,23,7,-1,18,23,42,37,2]

# Eng katta uchta elementni topish

print(heapq.nlargest(3,nums)) # Natija [42,37,23]

# Eng kichik uchta elenet
print(heapq.nsmallest(3, nums)) # Natija [-4,1,2]

