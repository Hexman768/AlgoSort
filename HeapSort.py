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
        if (left < n and self.array[left] > self.array[largest]):
            largest = left
        if (right < n and self.array[right] > self.array[largest]):
            largest = right
        if (largest != i):
            swap = self.array[i]
            self.array[i] = self.array[largest]
            self.array[largest] = swap
            self.heapify(n, largest)

