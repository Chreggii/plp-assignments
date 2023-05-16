class QuickSort():

    def __init__(self, array, lo, hi):
        self.array = array
        self.lo = lo
        self.hi = hi

    def sort(self):
        self.sortRecursive(self.array, self.lo, self.hi)

    def sortRecursive(self, array, lo, hi):
        if lo < hi:
            p = self.partition(array, lo, hi)
            self.sortRecursive(array, lo, p - 1)
            self.sortRecursive(array, p + 1, hi)

    def partition(self, array, lo, hi):
        pivot = array[hi]
        i = lo
        for j in range(lo, hi):
            if array[j] < pivot:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
                i += 1
        temp = array[i]
        array[i] = array[hi]
        array[hi] = temp
        return i
