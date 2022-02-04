class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.arr = [k, nums]

    def add(self, val: int) -> int:
        self.arr[1].append(val)
        li = self.arr[1]
        li.sort(reverse=True)
        return self.arr[1][self.arr[0] - 1]
