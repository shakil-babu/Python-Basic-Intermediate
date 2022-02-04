class KthLargest:
    def __init__(self, k, nums):
        self.arr = [k, nums]

    def add(self, val):
        self.arr[1].append(val)
        li = self.arr[1]
        li.sort(reverse=True)
        return self.arr[1][self.arr[0] - 1]


ans = KthLargest(3, [4, 5, 8, 2])

print(ans.arr)
print(ans.add(3))
