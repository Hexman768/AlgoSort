from BaseSort import BaseSort

class BubbleSort(BaseSort):
    def sort(self):
        sorted = False
        while not sorted:
            for i in range(len(self.array)-1):
                if (self.array[i] > self.array[i+1]):
                    self.swap(i, i+1)
            sorted = self.check_sort()
        return True
