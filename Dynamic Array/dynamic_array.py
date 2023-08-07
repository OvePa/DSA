import ctypes
import sys


class DynamicArray(object):
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, item):
        if not 0 <= item < self.n:
            return IndexError("Item is out of bounds!")

        return self.A[item]

    def append(self, ele):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)  # 2x if capacity isn't enough

        self.A[self.n] = ele
        self.n += 1

    def _resize(self, new_cap):
        B = self.make_array(new_cap)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()


if __name__ == "__main__":
    arr = DynamicArray()
    for i in range(100):
        arr.append(i)
        print("Length: ", len(arr))
        print("Size of array:", sys.getsizeof(arr))
