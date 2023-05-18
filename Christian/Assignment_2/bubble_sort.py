class BubbleSort():

    def __init__(self, array):
        self.array = array

    def sort(self):
        n = len(self.array)
        swapped = False

        # Traverse through all array elements
        for i in range(n-1):
            for j in range(0, n-i-1):

                # Swap if the element found is greater
                if self.array[j] > self.array[j + 1]:
                    swapped = True
                    self.array[j], self.array[j +
                                              1] = self.array[j + 1], self.array[j]

            if not swapped:
                # if we haven't needed to make a single swap, we can just exit the main loop.
                return
