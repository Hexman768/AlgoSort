from BaseSort import BaseSort

class HeapSort(BaseSort):
    def sort(self):
        l = len(self.array)
        for i in range(l // 2 - 1, -1, -1):
            self.heapify(l, i)
        for i in range(l-1, 0, -1):
            self.swap(0, i)
            self.heapify(i, 0)

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if (left < n and self.array[i] < self.array[left]):
            largest = left
        if (right < n and self.array[largest] < self.array[right]):
            largest = right
        if (largest != i):
            self.swap(i, largest)
            swap = self.array[i]
            self.heapify(n, largest)

