class SelectionSort():

    def __init__(self, array):
        self.array = array
        self.size = len(array)

    def sort(self):
        for ind in range(self.size):
            min_index = ind

            for j in range(ind + 1, self.size):
                # select the minimum element in every iteration
                if self.array[j] < self.array[min_index]:
                    min_index = j
            # swapping the elements to sort the array
            (self.array[ind], self.array[min_index]) = (
                self.array[min_index], self.array[ind])
