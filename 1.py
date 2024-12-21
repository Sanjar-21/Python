def so(items):
    head, *title = items
    return head + sum(title) if title else title

nums = [1,2,3,4,5,6,7,8,9]
print(sum(nums))
print(so(nums))